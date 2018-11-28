#include <bits/stdc++.h>
#define fast ios::sync_with_stdio(0);cin.tie(0);
#define fora(i,a,b) for(i=a;i<b;i++)
#define reva(i,a,b) for(i=a;i>=b;i--)

using namespace std;



int main(){
    fast
   // freopen("test.in","r",stdin);
    //freopen("output.in","w",stdout);

    int x=1;
	int t;
	cin>>t;
	for(x=1;x<=t;x++){
        cout<<"Case #"<<x<<": ";
           string a;
    int i,j,k,m,n,sum=0;
    cin>>a>>k;
    n=a.size();
    int st[n+1]={0};
    fora(i,0,n){
        if(a[i]=='+')
            sum++;
    }
    if(sum==n){
        cout<<"0\n";
		continue;
    }
	bool aa=false;
    int ct=0;
    while(1){
        int flag=0;
        fora(i,0,n){
            if(a[i]=='-'){
                if(i+k<=n){
                    if(st[i]==2){
                        if(sum==n){
                            cout<<ct<<endl;
                        }
                        else{
                            cout<<"IMPOSSIBLE\n";
                        }
						aa=true;
						break;
                    }
                    st[i]++;
                    fora(j,i,i+k){
                        if(a[j]=='-'){
                            sum++;
                            a[j]='+';
                        }
                        else{
                            sum--;
                            a[j]='-';
                        }
                    }
                    ct++;
                    if(sum==n){
                        cout<<ct<<endl;

						aa=true;
						break;
                    }
                    flag++;
                }
            }
        }
		if(aa)
			break;
        reva(i,n-1,0){
            if(a[i]=='-'){
                if(i+1-k>=0){
                    if(st[i]==2){
                        if(sum==n){
                            cout<<ct<<endl;
                        }
                        else{
                            cout<<"IMPOSSIBLE\n";
                        }

						aa=true;
						break;
						}
                    st[i]++;
                    reva(j,i,i+1-k){
                        if(a[j]=='-'){
                            sum++;
                            a[j]='+';
                        }
                        else{
                            sum--;
                            a[j]='-';
                        }
                    }
                    ct++;
                    if(sum==n){
                        cout<<ct<<endl;

						aa=true;
						break;
                    }
                    flag++;
                }
            }
        }
        if(!flag){
            cout<<"IMPOSSIBLE\n";
         break;
        }
		if(aa)
			break;
    }
    }

}
