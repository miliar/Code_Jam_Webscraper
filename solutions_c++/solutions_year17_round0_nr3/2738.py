#include <string>
#include <iostream>
#include <algorithm>

#include <map>

#include <boost/multiprecision/cpp_int.hpp> 

#define REP(i,n) for(int i = 0; i < n; ++i)

using namespace std;
typedef boost::multiprecision::cpp_int INT;




int  main(int argc, char** argv){
  int T;
  cin >> T;
  REP(i, T){
  INT N;
  INT K;
  cin >> N >> K;
  map<INT, INT> spaces;
  spaces[N] = 1;
  INT max, min;
   while (K > 0){
    INT n, s;
    auto it = spaces.rbegin();
    s = it->first;
    n = it->second;
    K -= n;
    spaces[min = (s/2 - ((s-1)%2))] += n;
    spaces[max = s/2] += n;
    spaces.erase(s);
    //cout << i+1 << ": " << max << " " << min << " K " << K << endl;
    }
   cout << "Case #" << i+1 << ": " << max << " " << min << endl;
  }  
  return 0;
}





long log2(long k){
  long res;
  while (k >>= 1) ++res;
  return res;
}

// struct node {
//   node *nl, *nr;
//   long size;
//   node(long n) : size(n), nl(NULL), nr(NULL) {}
//   void globalSplit(){
//     if(nl == NULL){
//       nl = new node(size / 2 - (size % 2));
//       nr = new node(size / 2);
//     } else {
//       nl->globalSplit();
//       nr->globalSplit();
//     }
//   }
//   long getMax(){
//     if(nl == NULL){
//       return size;
//     } else {
//       return max(nl->getMax(), nr->getMax());
//     }
//   }
//   bool splitSize(long n, bool todo = true){
//     if(todo and n == size and nl == NULL){
//       nl = new node(size / 2 - (size % 2));
//       nr = new node(size / 2);
//       return false;
//     } else {
//       nr->splitSize(n, nl->splitSize(todo));
//     }
//   }
// };
