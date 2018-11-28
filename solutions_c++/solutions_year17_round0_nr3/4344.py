#include <iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int main() {
    long long int i,n,k,a,b,f=0;
    int t;
    cin>>t;
    while(t--){
        f++;
        priority_queue<long long int> vec;
        cin>>n>>k;
        vec.push(n);
        while((k--)-1){
            if(vec.top()%2==0){
                vec.push(vec.top()/2);
                vec.push((vec.top()/2)-1);
            }
            else{
                vec.push(vec.top()/2);
                vec.push(vec.top()/2);
            }
            vec.pop();
            
        }
        cout<<"Case #"<<f<<": ";
        if(vec.top()%2==0)
              cout<<(vec.top()/2)<<" "<<(vec.top()/2)-1<<endl;
        else
              cout<<vec.top()/2<<" "<<vec.top()/2<<endl;
              
       
              
    }
 
	return 0;
}
