#include "iostream"
#include "cstdio"
#include "cstring"
#include "algorithm"
#include "string"
#include "cmath"
#include "vector"
#include "set"
#include "map"
#include "queue"
#include "stack"
using namespace std;
const int maxn=110;
bool judge(char ch){
	if(ch>='A'&&ch<='Z')
		return true;
	return false;
}
int main()
{
	freopen("A-large.in.txt", "r", stdin);  
    freopen("aa.txt", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		int R,C;
		string s[maxn];
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
				cin>>s[i][j];
		printf("Case #%d:\n",cas);
		for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
            {
                if(!judge(s[i][j])&& i>0)
                    s[i][j]=s[i-1][j];
            }


        for(int i=R-1;i>=0;i--)
            for(int j=0;j<C;j++)
            {
                if(!judge(s[i][j])&& i<R-1)
                    s[i][j]=s[i+1][j];
            }

        for(int j=0;j<C;j++)
            for(int i=0;i<R;i++)
            {
                if(!judge(s[i][j])&& j>0)
                    s[i][j]=s[i][j-1];
            }

        for(int j=C-1;j>=0;j--)
            for(int i=0;i<R;i++)
            {
                if(!judge(s[i][j])&& j<C-1)
                    s[i][j]=s[i][j+1];
            }
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++)
				cout<<s[i][j];
			cout<<endl;
		}
	}
}
