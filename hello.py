def build_ospf_config_1(vrf,rd, rt_export='', rt_import=''):
    rt_export = rd if not rt_export else rt_export
    rt_import = rd if not rt_import else rt_import
    return f"""
    vrf: {vrf}
    rd : {rd}
    rt_import : {rt_import}
    rt_export : {rt_export}
    """
print (build_ospf_config_1(1,2,3))