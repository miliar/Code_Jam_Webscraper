#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void flipK(string& s,int index,int k)
{
int t = index;
  while(t < index+k){
  	s.at(t) = (s[t]=='+')?'-':'+';
  	t++;
  }

}

bool headUp(string& s,int index)
{
   while(index < s.size()){
   	if(s[index]=='-')
   		return false;
   	index++;
   }

   return true;
}


int minCount(string& s,int k)
{
int count=0;
int index=0;

  while(index <= s.size()-k){
        if(s.at(index)=='-'){
        	flipK(s,index,k);
        	count++;
        }
        index++;
  }
  
  if(!headUp(s,index))
  	return -1;
  return count;
}


int main(){
    int t,k,c=0,ct;
    string s;
    cin >> t;

    while(t--){
    	c++;
    	cin >> s >> k;
        ct = minCount(s,k);
        if(ct==-1)
        	cout <<"Case #" << c << ": " <<"IMPOSSIBLE" << endl;
        else
        cout << "Case #" << c <<": " << ct << endl;

        s.clear();
    }

	return 0;
}