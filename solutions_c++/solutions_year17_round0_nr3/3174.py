#include <iostream>
#include <tuple>

using namespace std;

//Global variables
long long N,K;
const int stormax = 1000;
long long howmuch[stormax];
long long what[stormax];

//Function declarations
tuple<long long, long long, int, long long>  step(int i, long long allowed);

//////////////////////////////////////////////////
int main()
{
	int i,T,kva,ind;
	long long j, k, resmax, resmin;
	cin >> T;
  for (i=1; i<=T; i++){
  	cin>>N;
  	cin>>K;
		
		for(kva=0; kva<stormax; kva++){
			what[kva]=0;
			howmuch[kva]=0;
		}
		
		what[0]=N;
		howmuch[0]=1;
		ind=0;
		while(K>0){
	  	tie(resmax,resmin,ind,k) = step(ind,K);
	  	K-=k;
	  	//cout<<"resmax = "<<resmax<<", resmin = "<<resmin<<endl;
	  	if (resmax==0) break;
		}
		
		cout << "Case #" << i << ": " << resmax << " "<< resmin <<endl;
  }
  return 0;
}//end main
/////////////////////////////////////////////////////////

tuple<long long, long long, int, long long>  step(int i, long long allowed){
	long long resmax, resmin, howmuchtemp;
	int j;
	while (howmuch[i]==0) i+=1;
	howmuchtemp = min(howmuch[i],allowed);
	howmuch[i] -= howmuchtemp;
	resmax=what[i]/2;
	resmin=(what[i]-1)/2;
	for (j=i; j<stormax; j++){
		if (what[j]==0){
			what[j]=resmax;
			howmuch[j] = howmuchtemp;
			break;
		}
		if (what[j]==resmax){
			howmuch[j] += howmuchtemp;
			break;
		}
	}
	if (j==stormax) cout<<"Fubar"<<endl;
	for (j=i; j<stormax; j++){
		if (what[j]==0){
			what[j]=resmin;
			howmuch[j] = howmuchtemp;
			break;
		}
		if (what[j]==resmin){
			howmuch[j] += howmuchtemp;
			break;
		}
	}
	if (j==stormax) cout<<"Fubar"<<endl;
	return make_tuple(resmax,resmin, i, howmuchtemp);
}
	






