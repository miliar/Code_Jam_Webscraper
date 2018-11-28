#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

//string computeAns();
double computeAns(int N,int K,double U,vector<double> &prob);
#define For(i,st,en) for(int i=st;i<en;i++)
#define NFor(i,en,st) for(int i=en;i>=st;i--)

template<typename T> 
void Min(T &obj1,T obj2) {	
    	if(obj1 > obj2)
    	   obj1 = obj2;
}

template<typename T> 
void Max(T &obj1, T obj2) {	
    	if(obj1 < obj2)
    	   obj1 = obj2;
}

template<typename T>
bool comp(const T &o1, const T &o2) {
	if(o1 < o2)
	    	return true;
	else
	    	return false;	
}

int main() {

	int maxLoops;
	cin>>maxLoops;
	int  N,K;
	double U;
	For(loopNum,1,maxLoops+1) {

	    cin >>N>>K;
	    cin>>U;
	    vector<double> prob(N,0.00);

	    For(i,0,N)
		cin>>prob[i];

	    //declarations and input completed

	   double ans = computeAns(N,K,U,prob);

	    cout<<"Case #"<<loopNum<<": ";
	    printf("%.8lf\n",ans);
	}

	return 0;
}


double computeAns(int N,int K,double U,vector<double> &prob) {
	double ans;
	double sum=U;
	For(i,0,N) 
		sum +=prob[i];

	double avg = sum/N;

	sort(prob.begin(),prob.end());
	
	double Uleft =U;
	
	int st=0;
	while(Uleft>0.0000000001 && st<=N-2) {
//		cout<<"For this iteration,  st: "<<st<<" and Uleft: "<<Uleft<<endl;
	    if(prob[st]==prob[st+1])
		    {st++; continue;}

		double shift = prob[st+1]-prob[st];
		if( (st+1)*shift > Uleft) {
			
		    	For(i,0,st+1) {
				prob[i]=prob[i]+ (Uleft/(st+1));
			}
			Uleft=0;
			break;
		}

		For(i,0,st+1) {
			prob[i]=prob[st+1];
		}
		Uleft -= (st+1)*shift;
//		cout<<"prob["<<st<<"]: "<<prob[st]<<endl;
		st++;
	
	}
	For(i,0,st+1) {
		prob[i] = prob[i] + ( Uleft/(st+1));
	}

	
	double prod=1.000000000;
	
	For(i,0,N) {
//		cout<<"prob["<<i<<"]: "<<prob[i]<<endl;		
		prod *= prob[i]; 

	}
	return prod;
}
