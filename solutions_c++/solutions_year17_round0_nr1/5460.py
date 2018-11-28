#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<string>

#define lol long long
#define uol unsigned long long
#define lod long double

using namespace std;

string pan;
int ct = 0;
void flip(int start, int K){

 for(int i = start; i<=start+K-1; i++){
    if(pan[i]=='+')  pan[i] = '-';
    else pan[i] = '+';


 }  ct++;
   cout<<pan<<endl;
}


int check_happy(){

 for(int i = 0; i<pan.size(); i++){

    if(pan[i] == '+')
        continue;

    else
        return 0;


 }

  return 1;

}





int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T;
    int K; //int ct = 0;
    cin>>T;
    for(int i =0; i<T; i++){

      cin>>pan;
      //cout<<pan<<endl;


      cin>>K;
     // cout<<K<<endl;

      for(int j = 0; j < pan.size()-K+1; j++){
        if(pan[j] == '-'){
            flip(j, K);
           // j = j+K-2;
            }

      }

    if(check_happy()==0)
        cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    else
      cout<<"Case #"<<i+1<<": "<<ct<<endl;
    ct = 0;

    }




    return 0;
}
