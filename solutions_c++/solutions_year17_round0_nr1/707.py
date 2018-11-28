#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;


int main(){
	int nb;
	cin >>nb;
	for(int cases=0; cases<nb; cases++){
    cout << "Case #"<<cases+1<<": ";
    string s;
    long long k;
    cin>>s>>k;
    string s1(s);
    int moves1 =0;
    for(int i=0;i<=s1.size()-k;i++){
      if(s1[i]=='-'){
        moves1++;
        for(int j=i;j<i+k;j++)
          s1[j]='+'+'-'-s1[j];
      }
    }
    bool ok1 = true;
    for(int j=s1.size()-k;j<s1.size();j++) if (s1[j]=='-') ok1 = false;
    
    string s2(s);
    int moves2 =0;
    for(int i=0;i<=s2.size()-k;i++){
      if(s2[i]=='-'){
        moves2++;
        for(int j=i;j<i+k;j++)
          s2[j]='+'+'-'-s2[j];
      }
    }
    bool ok2 = true;
    for(int j=s2.size()-k;j<s2.size();j++) if (s2[j]=='-') ok2 = false;
    if(!ok2 && !ok1) cout << "IMPOSSIBLE"<<endl;
//     else cout << min (moves2, moves1)<<endl;
    else cout << moves1<<endl;
  }
	return 0;
}
