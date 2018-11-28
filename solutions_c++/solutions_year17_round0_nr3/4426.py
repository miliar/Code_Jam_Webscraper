/*input
100
4 2
5 2
6 2
1000 1000
1000 1
949792 714292
1000000 499998
891476 818518
500000 262143
500000 237856
264744 234245
500000 1
1000000 1000000
854838 706592
999999 505763
1000000 475713
494959 471175
477115 475297
288907 271880
999999 128
1000000 500000
3 2
999999 1
270333 254796
1000000 475712
999999 127
633911 497124
500000 131072
3 1
1000000 128
1000000 2
973446 751500
984463 918347
317717 256230
1000000 499999
628213 616543
1000000 524288
586142 492481
999999 499999
1000000 1
999999 999999
744628 638050
999999 262144
942895 867083
448626 366865
500000 237857
1000000 999999
999999 499997
999999 2
1000000 127
1000000 432558
999999 524288
500000 499999
314584 264447
999999 262143
999999 475711
1000000 523819
500000 243204
999999 499998
500000 2
708220 598371
558585 420639
936500 776178
986127 984765
486919 432443
4 1
500000 127
2 1
500000 249999
500000 131071
780505 685564
500000 500000
938305 893779
500000 128
999999 419746
500000 210868
999999 475712
5 1
999999 524287
711948 612854
500000 250000
1000000 262144
999999 999998
900230 711441
697315 554890
500000 262144
550404 430008
1000000 262143
470996 392214
1000000 524287
962880 746640
2 2
500000 249998
637871 526820
632066 599601
1 1
958179 733144
413549 393771
730378 704011
910033 850693
*/

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <math.h>
#include <algorithm>

int main()
{
	int T, n, flip_ct;
	T = 1;
	std::cin >> n;
	
	// Max Size
	int max_arr_size = 1000001;

	while (T <= n)
	{
		int N, K, cval;

		std::cin >> N;
		std::cin >> K;

		std::vector< std::vector<int> > Arr(max_arr_size, std::vector<int> (1, 0));
		int lv_idx, cmin, cmax;

		if (Arr[N][0]==0) {
			// build dp tree
			lv_idx = 1;
			std::vector<int> c_arr(1, N);
			std::vector<int> t_arr;
			Arr[N][0] = N;
			
			while (lv_idx < N) {

				for (int i=0; i < c_arr.size(); i++) {
					
					cval = c_arr[i]-1;
					cmin = floor(cval/2);
					cmax = cval - cmin;
					
					t_arr.push_back(cmax);
					t_arr.push_back(cmin);
				}
				lv_idx += c_arr.size() * 2;
				
				// Sorting the int vector
    			sort(t_arr.begin(), t_arr.end(), std::greater<int>());
    			Arr[N].insert(Arr[N].end(), t_arr.begin(), t_arr.end());

    			// clear t_arr
    			c_arr = t_arr;
    			t_arr.clear();
			}
		}

		// get kth node
		int node_val = Arr[N][K-1]-1;
		cmin = floor(node_val/2);
		cmax = node_val - cmin;
		
		std::cout << "Case #" << std::to_string(T++) << ": " << std::to_string(cmax) << " " << std::to_string(cmin) << '\n';
	}
}