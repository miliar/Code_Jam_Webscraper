#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cstring>
#include<cmath>
#include<cstdio>


#define lol long long
//#define uol unsigned long long
#define lod long double

using namespace std;

vector<lol> digits;
lol T,x;




lol power(lol base, lol index){
    lol ans = base;

    if(index == 0)
        return 1;
  for(lol i = 1; i<index; i++){

    ans = ans * base;


  }


   return ans;


}



lol cut_down(){
lol tru = 0;
for(lol i = digits.size()-1; i>=0; i--){
    if(digits[i] > digits[i-1]){
          for(int j = i-1; j>=0; j--)
              digits[j] = 0;
    }
}


  for(lol jk = 0; jk<digits.size(); jk++){
    lol place_value = (digits[jk]==0)? 0:digits[jk] * power(10,jk);
    cout<<"\nplace value of "<<jk<<" is "<<place_value<<endl;

    tru = tru + place_value;
  }

  cout<<"\nTrue starter is : "<<tru<<endl;




for(int i =0; i< 18; i++)
    cout<<"\n"<<digits[i]<<"\t";
cout<<"\n";

  return tru;
}


void split2(lol num){
  //digits.clear();



   for(lol i =0; i<=18; i++){


    lol x = num/power(10,i) % 10;                         //(num%(power(10,i)) - (num/power(10, i-1)))/power(10, i-1);
    cout<<x<<"\n";
    digits.push_back(x);
   }




     for(int i =0; i < 18; i++)
       cout<<digits[i]<<"\t";
     cout<<"\n";


}





int check_tid(){
int j;

 for( j = 0; j < 18; j++){
           if(digits[j] < digits[j+1]){
                digits.clear();
                return 0;
                //break;
           }

        } if(j == 18){
            digits.clear();
              return 1;
              //return i;
        }

return 1;





}


using namespace std;



int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    cin>>T;
    //ut<<T;


  for(int i = 0; i<T; i++){
      lol x;
       cin>>x;

       do{
       split2(x);
       x = cut_down();
       if(check_tid()==1)
        break;
       else
         x = x-1;

       digits.clear();}while(check_tid()!=1);


    cout<<"Case #"<<i+1<<": "<<x<<endl;
  }

  // lol k  = power(10,10);

  // cout<<k<<endl;  */



 //split2(1);
    return 0;
}
