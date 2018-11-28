#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <sstream> 
#include <string.h>
template <class ForwardIterator>
  bool is_sorted (ForwardIterator first, ForwardIterator last)
{
  if (first==last) return true;
  ForwardIterator next = first;
  while (++next!=last) {
    if (*next<*first)     // or, if (comp(*next,*first)) for version (2)
      return false;
    ++first;
  }
  return true;
}
using namespace std;
int istide(long long p){
	stringstream numby;
	string s;
	numby << p;
	numby>>s;
	return is_sorted(s.begin(),s.end());
}
int main(){
	int T,casee=1;
	long long N,tidy,aux;
	cin>>T;
	while(T--){
		cin>>N;
		tidy=N;
		while(!istide(tidy))tidy--;
		cout<<"Case #"<<casee<<": "<< tidy <<'\n';
		casee++;
	}
	return 0;
}