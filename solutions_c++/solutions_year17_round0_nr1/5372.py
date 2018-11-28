#include <iostream>

using namespace std;

int main() {
	
	int t,iteration;
	cin>>t;
	for(iteration=1;iteration<=t;iteration++)
	{
	    /*std::string str;
	    std::getline(std::cin, str);*/
	  char s[20];
	  int k,f=0,no=0,flag=0;
	  
	  cin>>s;
	  cin>>k;
	  int i=0;
	  while(s[i]!='\0'){
	      no++;
	      i++;
	  }
	  for(int i=0;i<no-k+1;i++)
	  {
	      if(s[i]=='-'){
	          f++;
	          for(int j=i;j<i+k;j++){
	            if(s[j]=='+'){
	                s[j]='-';
	            }  
	            else{
	                s[j]='+';
	            }
	          }
	      }
	  }
	  for(int i=0;i<no;i++)
	  {
	      if(s[i]=='-'){
	          flag=1;
	          break;
	      }
	  }
	  cout<<"Case #"<<iteration<<": ";
	  if(flag==1){
	      cout<<"IMPOSSIBLE"<<endl;
	  }
	  else{
	    cout<<f<<" "<<endl;    
	  }
	  
	}
	
	return 0;
}
