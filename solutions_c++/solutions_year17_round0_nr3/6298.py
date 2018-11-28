#include<bits/stdc++.h>
#define ll long long
using namespace std;
fstream in("C-small-2-attempt0.in", ios::in);
fstream out("bathroom1.out",ios::out);
class bath{
	public:
    static void solve(ll n,ll k,int i){
		double d=double(log(k)/(double)log(2));
        ll k1=(ll) d;
        ll k2=(ll) pow(2,k1);
        //cout<<k1<<" "<<k2<<endl;
       // System.out.println("k2: "+k2);
        ll require=(ll) (k-(k2-1));
        ll r=0;
        n=n-(k2-1);
        if((r=n%k2)!=0)
            n=(n/k2)+1;
        else
            n/=k2;
       // System.out.println(n+" "+require+" "+r);
       // System.out.println(n);
       if(r<require && r!=0){
        n--;}
		n--;
        //System.out.println(n);
       ll a=n/2;
       ll b=n-a;
       ll max=a>b?a:b;
       ll min=n-max;
       out<<"Case #"<<i<<": "<<max<<" "<<min<<endl;
        //System.out.println(max+" "+min);
    }
};
int main(){
	std::ios::sync_with_stdio(false);
	int tc;
	in>>tc;
	bath b;
	for(int i=1;i<=tc;i++){
		ll n,k;
		in>>n>>k;
		b.solve(n,k,i);
	}
	return(0);
}

