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
    libraries = {"std": True, "utils":True, }
    cdl_include_dirs = ["cdl"]
    export_dirs      = cdl_include_dirs + [ src_dir ]
    modules = []
    modules += [ CdlModule("de1_cl_controls")]
    # modules += [ CdlModule("picoriscv_de1_cl")]
    # modules += [ CdlModule("riscv_adjunct_de1_cl")]
    # modules += [ CdlModule("de1_cl_hps_debug")]
    # modules += [ CdlModule("de1_hps_debug")]
    modules += [ CdlModule("apb_target_de1_cl_inputs")]
    
    modules += [ CdlModule("tb_de1_cl_controls", src_dir=tb_src_dir)]
    # modules += [ CdlModule("tb_de1_cl_hps_debug.cdl")]
    # modules += [ CdlModule("tb_de1_cl_hps_generic.cdl")]
    # modules += [ CdlModule("tb_de1_hps_generic.cdl")]

