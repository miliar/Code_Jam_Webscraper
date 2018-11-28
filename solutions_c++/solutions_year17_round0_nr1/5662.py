#include <bits/stdc++.h>
using namespace std;

#define MAXS 1002

const int INF = (int)1e8;

char s[MAXS];
int k;

void init(){

}

unsigned long long solve(int indx){
	bool flag = true;
	unsigned long long result = 0;
	while(flag){
		while(s[indx] == '+'){
			indx++;
		}
		if(s[indx] == '\0'){
			flag = false;
		}
		else{
			for (int i = indx; i < indx+k; ++i)
			{
				if(s[i] == '\0'){
					result += INF;
					flag = false;
				}
				else if(s[i] == '+'){
					s[i] = '-';
				}
				else if(s[i] == '-'){
					s[i] = '+';
				}
				
			}
			indx++;
			result++;
		}
	}
	return result;
}

int main(){
	int T;
	unsigned long long ans;
	cin>>T;
	for (int j = 1; j <= T; ++j)
	{
		init();
		cin>>s>>k;
		ans = solve(0);
		cout<<"Case #"<<j<<": ";
		if(ans >= INF)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}



	return 0;
}