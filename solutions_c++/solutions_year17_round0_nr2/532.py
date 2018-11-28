#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;

ifstream in("B-large.in");
ofstream out("out-b.txt");

class xiomod{
	private: 
		streambuf *cin_stbuf;
		streambuf *cout_stbuf;
		
	public:
		xiomod();
		void redirect_input(string name);
		void redirect_ouput(string name);
		void restore_cin();
		void restore_cout();
 };

#define N 100009
#define ULL unsigned long long
#define LL long long

LL my_max(LL a, LL b){
	if(a>b)return a;
	return b;
}

LL check_n(LL n){
	vector<LL> v;
	LL m=n;
	while(n){
		v.push_back(n%10);
		n/=10;
	}

	LL prev=0;
	for(int i=v.size()-1; i>=0; i--){
		if(v[i]<prev){
			return 0LL;
		}
		prev=v[i];
	}

	return m;
}

LL biggest_n(LL n){
	vector<LL> v;
	while(n){
		v.push_back(n%10);
		n/=10;
	}

	LL prev=0;
	vector<LL> v2;
	bool flag=false;
	for(int i=v.size()-1; i>=0; i--){
		if(flag==true){
			v2.push_back(9);
		}else if(v[i]<prev){
			flag=true;
			//create space for 9
			for(int j=v2.size()-1, cnt=0; j>=0; j--){
				if(v2[j] == prev){
					v2[j]--;
					if(cnt>0 &&v[j]>0){
						v2[j+1]=9;
					}
					cnt++;
				}
			}
			v2.push_back(9);
		}else{
			prev=v[i];
			v2.push_back(v[i]);
		}
	}

	LL res=0;
    for(int i=0; i<v2.size(); i++){
        res*=10LL;
        res+=v2[i];
    }
	
    return res;
	
}

LL last_9(LL n){
	LL len=0;
	while(n){
		len++;
		n/=10LL;
	}
	LL res=0;
	for(LL i=1; i<len; i++){
		res*=10LL;
		res+=9LL;
	}

	return res;
}

int main()
{
	xiomod  ob;
	ob.redirect_ouput (string("out-b.txt"));
	ob.redirect_input (string("B-large.in"));

	//input
	LL t,n;
	cin>>t;

	for(int x=1; x<=t; x++){
		cin>>n;
		LL res=1;

		res = my_max(res, check_n(n));
		res = my_max(res, biggest_n(n));
		res = my_max(res, last_9(n));

		cout<<"Case #"<<x<<": "<<res<<endl;
	}

	
	return 0;
}

		xiomod::xiomod(){
			cin_stbuf=cout_stbuf=NULL;
		}
		void xiomod::redirect_input(string name){
			if(cin_stbuf!=NULL){
				return;
			}
			
			cin_stbuf=cin.rdbuf();
			cin.rdbuf(in.rdbuf());
		}

		void xiomod::redirect_ouput(string name){
			if(cout_stbuf != NULL){
				return;
			}
			
			cout_stbuf=cout.rdbuf();
			cout.rdbuf(out.rdbuf());
		}

		void xiomod::restore_cin(){
			if(cin_stbuf!=NULL){
				cin.rdbuf(cin_stbuf);
				cin_stbuf=NULL;
			}
		}

		void xiomod::restore_cout(){
			if(cout_stbuf!=NULL){
				cout.rdbuf(cout_stbuf);
				cout_stbuf=NULL;
			}
		}