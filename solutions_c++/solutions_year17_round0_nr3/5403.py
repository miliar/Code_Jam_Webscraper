#include<bits/stdc++.h>
#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))


typedef uint64_t lng;

using namespace std;
template<typename T>
void display(T first,T last){
	while(first!=last){
		cout<<*first++;
	}
	cout<<endl;
}

int main(){
	fstream f,o;
	f.open("C-small-1-attempt0.in");
	o.open("output.txt");
	int t;
	f >> t;
	int count=1;
	//cout<<t<<endl;
	for(int i=0; i<t; ++i){
		lng n,k;
		f>>n>> k;
		vector<lng> v{n};
		while(k!=1){
			auto m = max_element(begin(v), end(v));
			lng a = (*m)/2;
			//cout<<a<<endl;
			if((*m)%2==0){
				vector<lng> v2{a-1,a};
				v.erase(m);
				v.insert(m,v2.begin(),v2.end());
			}
			else{
				vector<lng> v2{a,a};
				v.erase(m);
				v.insert(m,v2.begin(),v2.end());
			}			
			--k;
			//display(begin(v), end(v));
		}
		lng y,z;
		auto m = max_element(begin(v), end(v));
		lng a = (*m)/2;
		if((*m)%2==0){
			z= min(a-1,a);
			y= max(a-1,a);
		}
		else{
			z=a;
			y=a;
		}
		if(a!=0)
			o<<"Case #"<<count<<": "<<y<<" "<<z<<"\n";
		else
			o<<"Case #"<<count<<": "<<"0 0"<<"\n";
		
		++count;
	}
	
}