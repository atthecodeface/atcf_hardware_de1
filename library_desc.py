import cdl_desc
from cdl_desc import CdlModule, CModel

class Library(cdl_desc.Library):
    name = "de1"
    pass

class DE1Modules(cdl_desc.Modules):
    name = "de1"
    c_src_dir   = "cmodel"
    src_dir     = "cdl"
    tb_src_dir  = "tb_cdl"
    include_dir = "cdl"
    libraries = {"std": True, "utils":True, }
    export_dirs = [ src_dir, include_dir ]
    modules = []
    modules += [ CdlModule("bbc_micro_de1_cl.cdl")]
    modules += [ CdlModule("bbc_micro_de1_cl_bbc.cdl")]
    modules += [ CdlModule("bbc_micro_de1_cl_io.cdl")]
    modules += [ CdlModule("de1_cl_controls.cdl")]
    modules += [ CdlModule("picoriscv_de1_cl.cdl")]
    modules += [ CdlModule("riscv_adjunct_de1_cl.cdl")]
    modules += [ CdlModule("de1_cl_hps_debug.cdl")]
    modules += [ CdlModule("de1_hps_debug.cdl")]
    modules += [ CdlModule("apb_target_de1_cl_inputs.cdl")]
    
    modules += [ CdlModule("tb_de1_cl_controls.cdl")]
    # modules += [ CdlModule("tb_de1_cl_hps_debug.cdl")]
    # modules += [ CdlModule("tb_de1_cl_hps_generic.cdl")]
    # modules += [ CdlModule("tb_de1_hps_generic.cdl")]

