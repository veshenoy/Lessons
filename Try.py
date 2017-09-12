#! /usr/bin/Python

file=open("testdata.txt","w")
val=310154003230000
for i in range (1,200001):
    file.write("/data/datapcrf/CPS_TEST_LOAD/cps_provs_mod.pl -target prod_sjc -action delete:credential=%d\n" % val)
    val+=1
