#include<bits/stdc++.h>
using namespace std;

int Bstall[10000000];

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int q;
    cin >>q;
    for(int x=1;x<=q;x++){
        memset(Bstall,0,sizeof(Bstall));
        int n,k,tow,ls,rs;
        cin >> n >> k;
        int p1=0,p2=(n+1);
        Bstall[p1]=1;
        Bstall[p2]=1;
        pair<int,int>maxi;
        for(int i=1;i <=k;i++)
        {
            int x1=0,x2=n+1;
            maxi=make_pair(x1,x1);
            for(int j=1;j<=n+1;j++){
                if(Bstall[j]==1){
                    if((j-x1)>((maxi.second - maxi.first)))
                        maxi = make_pair(x1,j);
                    x1=j;
                }
            }
			int temp=(maxi.second - maxi.first -1);
			tow= maxi.first + (( (temp%2) ==0 )?(temp/2) : ((temp/2 )+ 1));
			Bstall[tow] = 1;
			ls = tow - maxi.first - 1;
			rs = maxi.second - tow - 1;
        }
        cout<<"Case #"<<x<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<endl;
    }
}
