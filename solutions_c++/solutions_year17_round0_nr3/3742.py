#include<bits/stdc++.h>
using namespace std;
set< pair< int , int > > S;
int main(){
                  cin.sync_with_stdio(false);
                  ifstream cin("a.txt");
                  ofstream cout("b.txt");
                  int T , tt = 1;
                  cin >> T;
                  while(T--){
                            int N , K;
                            cin >> N >> K;
                             S.clear();
                             S.insert({ N , -1});
                             int Large , Small;
                             for(int i = 1 ; i <= K ; ++i ){
                                       int dist = (*(--S.end())).first;
                                       int index = -(*(--S.end())).second;
                                       S.erase(--S.end());
                                       int left = index;
                                       int right = index + dist - 1;
                                       int middle = (left + right)/2;
                                       if(left < middle)
                                       S.insert({middle - left , -left});
                                       if(middle < right)
                                       S.insert({right - middle , -(middle + 1)});
                                       if(i == K){
                                       Large = max(middle - left ,  right - middle);
                                       Small = min(middle - left ,  right - middle);
                                       }
                             }
                             printf("%d\n",tt);
                             cout << "Case #" << tt++ <<": " << Large <<" " << Small << endl;
                  }
    return 0;
}
