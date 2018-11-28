#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

ifstream infile("B-small-attempt.in");
ofstream outfile("Bs_sol.in");


int fnc2(int a, int b){
    int c=b%10;
    int k=0;

    b=b/10;
    while(b%10 == c){
       k++;
       b=b/10;
    }

//    b--;
    b=10*b+c-1;
    while(k>0){
        b=10*b+9;
        k--;
        }

    while(a>0){
        b=10*b+9;
        a=a/10;
        }
    return b;
    }

int func1(int a, int b, int c){
    if(a==0) {
       return(b);
       }
    if((a%10)>=c){
        return func1((a/10), 10*b+a%10 , a%10);
       }
    int k=fnc2(a,b);
    return k;

    }

int revers(int k){
    int g=0;
  //  int ad=0;
  //  while((k%10)==0){
  //      k=k/10;
  //      ad++;
  //      }
    while(k>0){
        g=10*g+(k%10);

        k=k/10;
        }
  //      cout<<"ad=  "<<ad<<endl;
    return g;
    }

/*int func3(int a){
    int b=0;
    int c=9;
    while(a>0){
        if(a%10 <= c){
            a=a/10;
            b=10*b+(a/10);
            c=a/10;
        }
        else {
            a=a/10;
            b=10*b+c;
            }
    return b;
    }
}*/

int main(){
    int line,num,op,rev,i,opr,rev2,op2;
    i=1;
    infile>>line;
    while(line--){
        infile>>num;
        if((num%10)==0)
            num--;
        rev=revers(num);
        op=func1(rev,0,0);
     //   rev2=revers(op);
     //   op2=func1(rev2,0,0);

        outfile<<"Case #"<<i<<": "<<op<<endl;
        i++;
    }
}


