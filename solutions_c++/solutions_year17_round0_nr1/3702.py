#include <string>
#include <iostream>

using namespace std;

const string IMP = "IMPOSSIBLE";

int solve(string& s, int k) {
	int res = 0;
	int n = s.size();
	for(int i=0; i<n; ++i)
	{
		if(i+k-1>n-1)
			break;
		if(s[i]=='+')
			continue;
		res++;
		for(int j=i; j<i+k; ++j) {
			if(s[j]=='-')
				s[j]='+';
			else
				s[j]='-';
		}
	}
	for(int i=0; i<n; ++i)
	{
		if(s[i]=='-')
			return -1;
	}
	return res;
}

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
	int k;
	char tmp[2001];
  scanf("%2000s %d", tmp, &k);
  string s = tmp;
	auto res = solve(s, k);
	if(res==-1)
    	printf("%s\n", IMP.c_str());
	else
    	printf("%d\n", res);
  }
  return 0;
}
