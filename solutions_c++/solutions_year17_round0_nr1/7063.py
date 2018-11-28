

#include <iostream>
#include <set> 
#include <iterator>
using namespace std;
string kswitch(string q, int j, int k){
	for (int i=j;i<j+k;i++){
		if (q[i]=='-') q[i]='+';
		else q[i]='-';
	}
	//cout<<q<<endl;
	return q;
}

int main()
{ int T, K, l,res;
string q;
//cout << "enter";
 cin >> T;
 for (int i=0;i<T;i++){
 	cin >> q; 
 	cin >> K;	
 	res=0;

 	for (int j=0;j<q.size()-K+1;j++){
 		if (q[j]=='-') {
		 res++;
		 q=kswitch (q,j,K);}
 	}
 	l=q.size()-K;			
 	while (q[l]=='+' && l<q.size()){
 		l++;
	 }
	if (l<q.size() )cout << "Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
	else cout << "Case #"<<i+1<<": "<<res<<endl;
 }



  return 0 ;}
  
  
