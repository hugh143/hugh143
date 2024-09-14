import pstats
p=pstats.Stats('output.profile')
p.sort_stats('cumulative').print_stats(20)