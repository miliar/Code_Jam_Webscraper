#include <math.h>
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int no_cases;
class pancake{
public:
	long R;
	long H;
	long Side;
};

vector<pancake> cake; 

bool cmp1(pancake p1, pancake p2){
	if (p1.R==p2.R)
		return p1.H>p2.H;
	return p1.R>p2.R;
}

bool cmp2(pancake p1, pancake p2){
	return p1.Side>p2.Side;
}

int main(){
	cin>>no_cases;
	cout<<fixed<<setprecision(8);
	for (int caseID=1; caseID<=no_cases; caseID++){
		cake.clear();
		int n, k;
		cin>>n>>k;
		long Ri, Hi;
		for (int i=0; i<n; i++){
			cin>>Ri>>Hi;
			pancake p;
			p.R=Ri;
			p.H=Hi;
			p.Side=2*Ri*Hi;
			cake.push_back(p);
		}

		double rt=0;
		while (cake.size()>=k){
			double temp=0;
			sort(cake.begin(), cake.end(), cmp1);
			long radius=cake[0].R;
			long height=cake[0].H;
			temp=temp+M_PI*radius*radius+2*M_PI*radius*height;
			cake.erase(cake.begin()+0);
			sort(cake.begin(), cake.end(), cmp2);

			for (int i=0; i<k-1; i++){
				temp+=cake[i].Side*M_PI;
			}
			if (temp>rt)
				rt=temp;
		}
		cout<<"Case #"<<caseID<<": "<<rt<<endl;

	}
}