# eophis API
import eophis
# other modules
import argparse

def ocean_info():
    # ocean namelist
    nemo_nml = eophis.FortranNamelist('/home/jdoe/morays_tutorial/nemo_v4.2.1/cfgs/C1D_PAPA32/EXPREF/namelist_cfg')

    # step 1: define exchanges
    tunnel_config = list()
    tunnel_config.append( { 'label' : 'TO_NEMO', \
                            'grids' : {}, \
                            'exchs' : [ {} ] }
                        )

    # step 2: tunnel registration
    # ...
                        
    return to_nemo, nemo_nml


def preproduction():
    eophis.info('========= C1D_PAPA32.ASFC : Pre-Production =========')
    eophis.info('  Aim: write coupling namelist\n')

    # ocean info
    to_nemo, nemo_nml = ocean_info()
    
    # step 3: get info from NEMO namelist
    step, it_end, it_0 = # ...
    total_time = (it_end - it_0 + 1) * step

    # step 4: write OASIS namelist
    # ...


def production():
    eophis.info('========= C1D_PAPA32.ASFC : Production =========')
    eophis.info('  Aim: execute coupled simulation\n')

    #  Ocean Coupling
    # ++++++++++++++++
    to_nemo, nemo_nml = ocean_info()

    step, it_end, it_0 = nemo_nml.get('rn_Dt','nn_itend','nn_it000')
    niter = it_end - it_0 + 1
    total_time = niter * step

    # step 5: deploy OASIS interface
    # ...

    #  step 6: import ASFC
    # +++++++++++++++++++++
    # ...

    #  step 7: Time synchronization
    # ++++++++++++++++++++++++++++++
    @eophis.all_in_all_out( # ... )
    def loop_core(**inputs):
        
        # step 8: connect exchanged fields with ASFC
        outputs = {}
        outputs['an_output'] = a_model( inputs['an_input'] )
        return outputs

    #  Run
    # +++++
    eophis.starter(loop_core)
    
# =========================== #
if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--exec', dest='exec', type=str, default='prod', help='Execution type: preprod or prod')
    args = parser.parse_args()

    eophis.set_mode(args.exec)

    if args.exec == 'preprod':
        preproduction()
    elif args.exec == 'prod':
        production()
    else:
        eophis.abort(f'Unknown execution mode {args.exec}, use "preprod" or "prod"')
