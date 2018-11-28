#include <iostream>
#include <string>
#include <queue>
#include <stack>

using namespace std;

int main(){
  int t,cont,k;
  string in;
  bool salir;
  
  cin>>t;

  for(int i=1;i<=t;i++){
    cin>>in>>k;
    stack<bool> s;
       
    for(int j=0; j<in.length(); j++){
      if(in[j] == '+')
	s.push(1);
      else
	s.push(0); 
    }
    cont=0;
    salir=false;
    while(!s.empty() && !salir){
      if(s.top())
	s.pop();
      else if(s.size()>=k){
	cont++;

	stack<bool> aux;

	for(int l=0;l<k;l++){
	  aux.push(s.top());
	  s.pop();
	}
	
	while(!aux.empty()){
	  s.push(!aux.top());
	  aux.pop();
	}
      }else
	salir=true;
    
       
    }
    cout<<"Case #"<<i<<": ";
    if(s.empty())
      cout<<cont;
    else
      cout<<"IMPOSSIBLE";
    cout<<endl;
    
  }
  
  
  return 0;
}
