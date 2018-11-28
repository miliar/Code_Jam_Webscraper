#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		int R,C;
		char str[30][30];
		cin>>R>>C;
		for(i=0;i<R;i++) cin>>str[i];
		vector<int> vt[25];
		for(i=0;i<C;i++){
			for(j=0;j<R;j++)
			{
				if(str[j][i]!='?')vt[i].push_back(j);
			}
		}
		for(i=0;i<C;i++) {
			for(j=R-1;j>=0;j--) {
				if(str[j][i]=='?') {
					if(j<R-1 && str[j+1][i]!='?')str[j][i]=str[j+1][i];
					else {
						for(k=j-1;k>=0 && str[k][i]=='?';k--);
						if(k<0)break;
						str[j][i]=str[k][i];
					}
				}
			}
		}
		for(i=C-1;i>=0;i--) {
			for(j=R-1;j>=0;j--) {
				if(str[j][i]=='?') {
					if(i<C-1 && str[j][i+1]!='?')str[j][i]=str[j][i+1];
					else {
						for(k=i-1;k>=0 && str[j][k]=='?';k--);
						if(k<0)break;
						str[j][i]=str[j][k];
					}
				}
			}
		}
		cout<<"Case #"<<cs<<": \n";
		for(i=0;i<R;i++)cout<<str[i]<<endl;
	}
	return 0;
}
