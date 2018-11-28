#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("large.out","w",stdout);
	
	int task; scanf("%d", &task);
	for (int cs=1; cs<=task; cs++){
		char s[1100];
		int k;
		scanf("%s %d", s, &k);
		vector<int> data(0);
		for (int i=0; i<strlen(s); i++){
			if (s[i]=='+')
				data.push_back(1);else
				data.push_back(0);
		}
		
		int result = 0;
		for (int i=0; i<data.size(); i++)
		if (data[i]==0){
			if (i+k-1 >= data.size()){
				result = -1;
				break;
			}else{
				result++;
				for (int j=i; j<=i+k-1; j++)
					data[j] ^= 1;
			}
		}

		if (result == -1)
			printf("Case #%d: IMPOSSIBLE\n", cs);else
			printf("Case #%d: %d\n", cs, result);
	}	
	return 0;
}
