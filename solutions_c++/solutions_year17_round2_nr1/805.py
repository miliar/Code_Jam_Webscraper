#include<stdio.h>

int main(int argc, char** argv) {
	if (argc != 3) return 0;
	FILE* input;
	FILE* output;
	input = fopen(argv[1],"r");
	output = fopen(argv[2],"w");
	int t;
	fscanf(input,"%d",&t);
	for (int z = 0;z < t;++z) {
		int d;
		int n;
		fscanf(input,"%d",&d);
		fscanf(input,"%d",&n);
		double max_time = 0.0;
		for (int j = 0;j < n;++j) {
			int hp;
			int hs;
			fscanf(input,"%d",&hp);
			fscanf(input,"%d",&hs);
			double time = ((double) (d - hp))/hs;
			if (max_time < time) max_time = time;
		}
		double ans = ((double) d)/max_time;
		fprintf(output,"Case #%d: %lf\n",z+1,ans);
	}
}
