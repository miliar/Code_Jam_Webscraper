#include <stdio.h>
#include <string.h>

int main() {

	freopen("B-large.in", "r", stdin);

	setbuf(stdout, NULL);

	FILE *fp = fopen("output.txt", "w");

	int T;
	scanf("%d", &T);
	for  (int k = 1; k <= T; k++)
	{
		char num[20];
		char *result;
		scanf("%s", num);
		int len = strlen(num);
		for (int i = 0; i < len - 1; i++)
		{
			if (i < 0)
				break;
			if (num[i] > num[i + 1])
			{
				for (int j = i + 1; j < len; j++)
					num[j] = '9';
				num[i]--;
				len = i + 1;
				i -= 2;
				
			}
		}
		if (*num == '0')
			result = num + 1;
		else
			result = num;
		char ret[1024];
		snprintf(ret, sizeof(ret),  "Case #%d: %s\n", k, result);
		fwrite(ret, 1, strlen(ret), fp);
		
	    printf("%s\n", result);
		
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