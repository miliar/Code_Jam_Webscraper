#include <stdio.h>
#include <iostream>
#include <queue>
#include <string.h>

using namespace std;

int main() {

	freopen("C-large.in", "r", stdin);

	setbuf(stdout, NULL);

	FILE *fp = fopen("output.txt", "w");

	int T;
	scanf("%d", &T);
	for  (int ee = 1; ee <= T; ee++)
	{
		long long n, k, min = 9000000000000000000L, max = -1;
		long long arr[2][2];
		scanf("%lld%lld", &n, &k);
		

		arr[0][0] = n - 1;
		arr[0][1] = 0;
		arr[1][0] = n;
		arr[1][1] = 1;


		long long count = 1;
		long long final_k;
		long long ori_k = k;
		while (1)
		{
			if (k == 1)
			{
				final_k = ori_k - count + 1;
				break;
				//end
			}
			k /= 2;
			count*=2;
			
			if (arr[1][0] % 2 == 1)
			{
				arr[1][1] = arr[1][1] * 2;
				arr[1][1] += arr[0][1];
			}
			else
			{
				arr[0][1] = arr[0][1] * 2;
				arr[0][1] += arr[1][1];
			}
			arr[1][0] = arr[1][0] / 2;
			arr[0][0] = arr[1][0] - 1;
		}
	
		long long big = arr[0][0], small = arr[1][0];
		long long bigc = arr[0][1], smallc = arr[1][1];
		if (arr[1][0] > arr[0][0])
		{
			big = arr[1][0];
			bigc = arr[1][1];
			small = arr[0][0];
			smallc = arr[0][1];
		}
		long long real_final = big;
		if (bigc - final_k < 0)
		{
			real_final = small;
		}
		max = real_final / 2;
		min = max;
		if (real_final % 2 == 0)
			min--;

		char ret[1024];
		snprintf(ret, sizeof(ret), "Case #%d: %lld %lld\n", ee, max, min);
		fwrite(ret, 1, strlen(ret), fp);
		printf("%s", ret);
	    
		
	}
	fclose(fp);
}
/*
100
132
1000
7
823
103
308
332
312
388
849
992
54
946
743
200
245
999
157
214
587
165
660
78
872
974
673
672
196
729
810
568
931
458
4
754
1
580
159
141
471
561
753
226
130
744
690
883
920
522
880
509
217
168
991
676
783
975
916
128
32
764
292
357
581
596
711
435
125
637
791
705
428
602
438
178
25
795
179
560
405
881
193
927
377
318
755
302
389
104
506
938
502
887
899
740
444
839
585
334
289


*/