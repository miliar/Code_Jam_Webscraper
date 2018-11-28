#include<cstdio>
#include<vector>

namespace {
	using std::vector;

	int calculate(vector<bool>& array, int n, int k) {
		int ans = 0;
		for (int i = 0;i <= n-k;++i) {
			if (!array[i]) {
				++ans;
				for (int j = i;j < i + k;++j) {
					array[j] = !array[j];
				}
			}
		}
		for (int i = 0;i < n;++i) {
			if (!array[i]) return -1;
		}
		return ans;
	}
}

int main() {
	FILE* input;
	FILE* output;
	input = fopen("A-large.in","r");
	output = fopen("pancakes_output_large.txt","w");
	int num;
	fscanf(input,"%d",&num);
	for (int i = 0;i < num;++i) {
		vector<bool> values;
		char* s = new char[5000];
		fscanf(input,"%s",s);
		int q = 0;
		while (s[q]) {
			if (s[q] == '+') values.push_back(true);
			else values.push_back(false);
			++q;
		}
		int k;
		fscanf(input,"%d",&k);
		int ans = calculate(values,values.size(),k);
		if (ans > -1) {
			fprintf(output,"Case #%d: %d\n",i+1,ans);
		} else {
			fprintf(output,"Case #%d: IMPOSSIBLE\n",i+1);
		}
	}
}
