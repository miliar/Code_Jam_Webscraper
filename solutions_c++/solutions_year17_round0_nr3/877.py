#include<iostream>
#include<fstream>
#include<string>
//#include<sstream>
#include<vector>
#include <stdlib.h>     /* atoi */
#include<algorithm>
#include<cassert>
#include<climits>
using namespace std;
#define MYMOD 1000000007
int num_ins(int c){
   int t = c;
   
   return c;
}
int num_ins(int c, int _r, int _c){
   return (_r - c)*(_c - c)*num_ins(c);
}
long long _mul(long long a, long long b){
   a%=MYMOD;
   b%=MYMOD;
   return (a*b)%MYMOD;
}
long long _solve_int_min(long long _i){
   if(_i%2 == 1){
      return _i/2;
   }
   else{
      return (_i/2) - 1;
   }
}
long long _solve_int_max(long long _i){
   if(_i%2 == 1){
      return _i/2;
   }
   else{
      return (_i/2);
   }
}
long long _solve(long long _n, long long _k){
   if(_n == _k){
      return 1;
   } 
   
   if(_k == 1){
      return (_n);
   }
   else if (_k == 2){
      return _n/2;
   }
   else{
      assert(_k > 0);
      if(_n%2 == 1){
         if(((_k-2)%2) == 0){
            return _solve(_n/2, ((_k-2)/2)+1);
         }
         else{
            return _solve(_n/2, ((_k-2)/2)+1);
         }
      }
      else{
         if(((_k-2)%2) == 0){
            return _solve(_n/2, ((_k-2)/2)+1);
         }
         else{
            return _solve((_n/2) - 1, ((_k-2)/2)+1);
         }
         
      }
   }
   /*
   long long ans = 0;
   long long large = 1000000;
   my_obj my(0,_n, _k);
   while(_k > 0){
      long long test_n = my._r;
      my._c2 = new my_obj(0, test_n/2,0);
      if(test_n%2 == 0){
         my._c1 = new my_obj(0, test_n/2 - 1,0);
      }
      else{
         my._c1 = new my_obj(0, test_n/2,0);
      }
      if(_k > 3){
      }
      else{
         if(test_n%2 == 0){
            return *(my._c2);
         }
         else{
            return *(my._c1);
         }
      }
      --_k;
   }
   list<my_obj> _arr;
   {
      my_obj my(-1,-1, 0);
      my_ans aa(-1,-1);
      my._ans = aa;
      _arr.push_back(my);
   }
   {
      my_obj my(0,1, 1);
      my_ans aa(0,1);
      my._ans = aa;
      my_obj& _pre = _arr.back();
      _arr.push_back(my);
      _pre._next = (&((_arr.back())));
      if(_n == 1){
         return aa;
      }
   }
   {
      my_obj my(0,2, 2);
      my_ans aa(0,2);
      my._ans = aa;
      my_obj& _pre = _arr.back();
      _arr.push_back(my);
      _pre._next = (&((_arr.back())));
      if(_n == 2){
         return aa;
      }
   }
   for(long long i = 3; i + 1 < (_n % large); ++i){
      if(i%2 == 0){
         long long _preidx = i -1;
         _arr(i) = my_obj(0,i,i);
         _arr(i)._c1 = _arr(_preidx)._c1; 
         _arr(i)._c2 = _arr(i)._c1->_next; 
         _arr(_preidx)._next = &(_arr(i));
         _arr(i)._next = NULL;
         _arr(i).cal_ans();
      }
      else{
         long long _preidx = i -1;
         _arr(i) = my_obj(0,i,i);
         //_arr(i)._idx = i;
         _arr(i)._c1 = (_arr(_preidx)._c2);
         _arr(i)._c2 = (_arr(_preidx)._c2);
         _arr(i)._next = NULL;
         _arr(_preidx)._next = &(_arr(i));
         _arr(i).cal_ans();
         //long long t_l = (i/2);
         //_arr(i) = _arr(t_l);
      }
   }
   for(long long i = (_n % large) - 1; i < (_n % large); ++i){
      if(i%2 == 0){
         long long t_l = (i/2) - 1;
         long long t_r = (i/2);
         bool bet = better(_arr(t_r), _arr(t_l) );
         if(bet){
            _arr(i) =  _arr(t_r);
         } 
         else{
            _arr(i) = _arr(t_l);
         }
      }
      else{
         long long t_l = (i/2);
         _arr(i) = _arr(t_l);
      }
      return _arr(i);
   }
   return _arr(0);
   */
}
long long _solve_new(long long _n, long long _k){
   if(_n == _k){
      return 1;
   } 
   if(_k == 1){
      return (_n);
   }
   else if (_k == 2){
      return _n/2;
   }
   else{
      assert(_k > 0);
      while (_k > 2){
         if(_n == _k){
            return 1;
         }
         if(_n%2 == 1){
            if(((_k-2)%2) == 0){
               _n = _n/2;
               _k = ((_k-2)/2)+1;
               //return _solve(_n/2, ((_k-2)/2)+1);
            }
            else{
               _n = _n/2;
               _k = ((_k-2)/2)+1;
               //return _solve(_n/2, ((_k-2)/2)+1);
            }
         }
         else{
            if(((_k-2)%2) == 0){
               _n = _n/2;
               _k = ((_k-2)/2)+1;
               //return _solve(_n/2, ((_k-2)/2)+1);
            }
            else{
               _n = (_n/2) - 1;
               _k = ((_k-2)/2)+1;
               //return _solve((_n/2) - 1, ((_k-2)/2)+1);
            }
            
         }
         
      }
      return _solve(_n, _k);
   }
}
int main(int argc, char* argv[]){
   ifstream data_in;
   ofstream data_out;
   data_in.open(argv[1]);
   data_out.open(argv[2]);
   int num_c = 0;
   data_in >> num_c;
   
   for(int i = 0; i < num_c;++i){
      long long _n;
      data_in >> _n;
      long long _k;
      data_in >> _k;
      long long ans = 0;
      long long _inter = 0;
      _inter = _solve_new(_n, _k);
      long long ans_max = _solve_int_max(_inter);
      long long ans_min = _solve_int_min(_inter);
      data_out<<"Case #"<<(i+1)<<": "<< ans_max<<" "<<ans_min<<endl;
   }
   data_in.close();
   
   data_out.close();
}
