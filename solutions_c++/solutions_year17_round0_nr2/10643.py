#include <iostream>
#include <vector>

using namespace std;
vector<int> v;
void solve(){
    for(size_t i = v.size(); i > 0; i--){
        int right = v[i];
        int left = v[i-1];
        if(left > right){
            v[i-1]--;
            for(size_t x = i; x < v.size(); x++ ){
                v[x] = 9;
            }
        }
    }
}
int main()
{
   
   int n;
   
   cin >> n;
   for(int i = 1; i <= n; i++){
       string x;
       int t = 0;
       cin >> x;
       while(x[t] != '\0'){
           v.push_back(x[t]-'0');
           t++;
       }
       
       solve();
       
       size_t j = 0;
       if(v[0] == 0) j = 1;
      
       cout << "Case #" << i << ": ";
        for(; j < v.size(); j++){
            cout << v[j];
        }
        cout << "\n";
        v.clear();
   }
   
   return 0;
}

