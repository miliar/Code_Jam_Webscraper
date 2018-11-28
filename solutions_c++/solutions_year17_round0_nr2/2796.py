#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define FOR(i,a,b) for(int i=a;i<b;i++)
using namespace std;
typedef unsigned long long ull;

bool isInOrder(ull num){
  ull last_digit = -1;
  while(num){
    ull remainder = num%10;
    if(last_digit==-1){
      last_digit = remainder;
    }else{
      if(remainder>last_digit){
	return false;
      }else{
	last_digit = remainder;
      }
    }
    num = (num/10);
  }
  return true;
}

ull getTidyNum(ull num){
  ull divider = 10;
  ull new_num = num;
  while(true){
    if(isInOrder(new_num)){
      break;
    }
    ull left_element = (new_num/divider);
    if(left_element == 0){
      break;
    }
    ull remainder = new_num%divider;
    if (remainder < (divider-1)){
      new_num = (((left_element-1)*divider) + (divider-1));
    }
    divider *= 10;
  }
  return new_num;   
}

int main(){
  //freopen("input.txt","r",stdin);
  //freopen("output.txt","w",stdout);
  int tt;
  cin>>tt;
  FOR(ttnum,1,tt+1){
    ull val;
    cin>>val;
    ull result = getTidyNum(val);
    cout<<"Case #"<<ttnum<<": "<<result<<endl;
  }
  return 0;
}
    
