#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<map>
#include<cstring>
#include<set>
using namespace std;
#define uii long long int
#define M(a,b) (a>b ? a : b)
#define m(a,b) (a>b ? b : a)
#define it(a)  ::iterator a
#define slld(a) uii a;scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define plld(a) printf("%lld",a)
#define MAX 10000
#define MOD 1000000007
#define powOf2(a) !(a&a-1)
#define mod(a) (a>0 ? a : (-1*a))
#define tc(a) uii a; for(scanf("%lld",&a);a--;)
#define swap(a,b) a = a^b; b = a^b;a = a^b;
#define toInt(a) (a-'0')
string sub(string a,string b){
	int borrow = 0;
	uii len = a.size();
	uii lenb = b.size();
	if(len > lenb){
		string b_i = "";
		for(uii i = 0;i<len-lenb;i++){
			b_i += "0";
		}
		b_i += b;
		b = b_i;
	}
	for(uii i = len-1;i>=0;i--){
		uii sum = toInt(a[i]) - toInt(b[i]) - borrow;
		//cout<<"sum : "<<sum<<endl;
		borrow = 0;
		if(sum<0){
			sum += 10;
			//cout<<sum<<endl;
			borrow = 1;
		}
		a[i] = sum+'0';
	}
	if(borrow != 0) a[0] = (toInt(a[0]-borrow))+'0';
	uii count = 0;
	while(a[count] == '0'){
		count++;	
	}
	string temp(a,count);
	return temp;
}
string toString(uii a){
	string s = "";
	string g = " ";
	while(a!=0){
		g[0] = (a%10)+'0';
		s+=g[0];
		a = a/10;
	}
	uii len =  s.size();
	string b = "";
	for(uii i = len-1;i>=0;i--){
		b+= s[i];	
	}
	return b;
}
int main(){
	uii T_case= 1;
	tc(T){
		string s;
		cin>>s;
		cout<<"Case #"<<(T_case)<<": ";
		T_case++;
		uii slen = s.size();
		uii n = 0;
		uii current = slen-1;
		for(uii i = slen-1;i>=0;i--){
			if(s[i-1]>s[i]){
				//cout<<s<<endl;
				string a = "";
				//cout<<s[i];
				a = ((toInt(s[current])+1)+ '0' );
				current--;
				for(uii j = 0;j<n;j++){
					a+="0";
				}
				n++;
				i++;
				//cout<<"s : "<<s[i]<<" "<<a<<endl;
				s = sub(s,a);
			}
			
			
		}
		
		cout<<s<<endl;

		
	}     
   




	return 0;
}


