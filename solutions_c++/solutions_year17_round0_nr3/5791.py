#include <iostream>
#include <list>

using namespace std;

void print_spaces(int n){
  cout << n-1-(n-1)/2 << " " << (n-1)/2 << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  int n, k;
  list<int>::iterator it;
  int s, i, max_l, cur_l, prev, i_best;
  int f_max_l;
  for(int ind=0; ind<T; ind++){
    cin >> n >> k;
    list<int>mylist;
    mylist.push_back((n-1)/2);
    for(int j=1; j<k;j++){
      //cout << "j = " << j << ", mylist size = " << mylist.size() << endl;
      //cout << "mylist = ";
      //for(it=mylist.begin(); it!=mylist.end(); ++it)
        //cout << *it << " ";
      //cout << endl;
      it = mylist.begin();
      max_l = *it;
      prev = *it;
      ++it;
      i_best = -1;
      i=0;
      //cout << "\t max_l = " << max_l << endl;
      while(it!=mylist.end()){
        cur_l = *it-prev-1;
        //cout << "\t i  = " << i << ", cur_l = " << cur_l << endl;
        if(cur_l>max_l){
          i_best = i;
          max_l = cur_l;
        }
        prev=*it;
        ++it;
        ++i;
      }      
      if(n-1-prev > max_l){
        //cout <<"\t lastly, cur_l = " << n-1-prev << endl;
        i_best = i;
        max_l = n-1-prev;
      }
      //cout << "\t finally, max_l = " << max_l << endl;
      f_max_l = max_l;
      //cout << "\t i_best = " << i_best << endl;
      if(i_best>=0){
        it = mylist.begin();
        for(int t=0; t<i_best; t++) ++it;
        int val = *it;
        ++it;
        mylist.insert(it, val+(max_l+1)/2);
        //cout << "j = " << j << ", inserted " << (val+(max_l+1)/2) << endl;
      } else{
        mylist.push_front((*mylist.begin()-1)/2);
        //cout << "j = " << j << ", inserted " << ((*mylist.begin()-1)/2) << endl;
      }
    }
    cout << "Case #" << (ind+1) << ": ";
    if(k==1){
      f_max_l = n;
    }
    print_spaces(f_max_l);
  }
  return 0;
}