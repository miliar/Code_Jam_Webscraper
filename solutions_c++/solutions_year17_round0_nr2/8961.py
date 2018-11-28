#include<iostream>
#include<string>
using namespace std;

int main() {
	freopen("i.txt","r",stdin);
	long long int n, ii, x, t[4] = {129, 999, 7, 99999999999999999};
	string y, o;
	cin>>n;
	for(long long int i=1; i<=n; i++) {
		cin>>x;
		o="";
		cout<<"Case #"<<i<<": ";
		y=to_string(x);
		int f=1;
		for(long long int iii=0; iii<y.length(); iii++) 
			if(f){
				if(y[iii]>y[iii+1] && iii<y.length()-1) {
					if(y[iii]-'1' < y[iii-1]-'0'){
						int iv, ivv;
						for(iv=iii, ivv=0; y[iv-1] == y[iii] && iv>0; iv--, ivv++) { o.pop_back(); }
						if((int)(y[iii-1]-'1')) o+=to_string((int)(y[iii-1]-'1')); for(int ff=0; ff<y.length()-iii+ivv-1; o+="9", ff++); 
						break;
					} else if(y[iii]-'1')
						o+=to_string((int)(y[iii]-'1')), f=0;
					else { o=""; for(int ff=0; ff<y.length()-1; o+="9", ff++); 
						break;}
				}  else o+=y[iii];
			} else o+="9";
		cout<<o<<endl;
	}
	return 0;
}	