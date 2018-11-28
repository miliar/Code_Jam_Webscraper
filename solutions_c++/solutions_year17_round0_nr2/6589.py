#include <bits/stdc++.h>
#define ll long long
using namespace std;

int getNum(char ch){
	return ch-48;
}
char getChar(int n){
	return char(n+48);
}

string all9(string p,ll ind,ll l){

	ll i;
	for(i=ind;i<l;i++){
		p = p + getChar(9);
	}
	return p;

}
main(){
	ll t,i,j,k,x=1,n1,n2,l,lp,ind,f;
	string s,p,temp;
	cin>>t;
	while(t--){
		cin>>s;
		f=0;
		p="";
		l = s.length();
		s = s+getChar(10);
		for(i=0;i<l;i++){
		
			n1 = getNum(s[i]);
			n2 = getNum(s[i+1]);
		
			if(n1<n2){
				p = p+s[i];
			}
			else if(n1>n2){
				if(n1-1!=0)
					p = p + getChar(n1-1);
			    p = all9(p,i+1,l);
			    break;
			}
			else if(n1==n2){
				temp = s[i];
				ind = i;
				for(k=i;k<l-1;k++){
					if(s[k]!=s[k+1]){
						f=k+1;
						break;
					}
					temp = temp + s[k];
					
				}
				i=k;
					if(k==l-1){
						p = p+temp;
						break;
					}
					else{
						if(getNum(s[ind])>getNum(s[f])){
							if(getNum(s[ind])-1!=0)
								p = p + getChar(getNum(s[ind])-1);
			    			p = all9(p,ind+1,l);
			    			break;
						}
						else
							p = p + temp;
					}
						
				}
			}
				
		cout<<"Case #"<<x<<": "<<p<<endl;
		x++;
	}
}