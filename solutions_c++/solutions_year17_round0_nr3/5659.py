#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<cstring>
#include<cmath>
#include<cstdio>


#define lol long long
#define uol unsigned long long
#define lod long double

using namespace std;



vector<lol> occupied;


lol T;

lol N,K;


lol greatest_diff(){
   lol greatest=0, index = -1;;
  for(int i = 0; i<occupied.size()-1; i++){

       if((occupied[i+1] - occupied[i] ) >  greatest){
           greatest = occupied[i+1] - occupied[i];
           cout<<"\nGreatest is "<<greatest<<"\n";
           index = i;
       }
   }

   cout<<"index is "<<index<<endl;
   return index;

}




int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    cin>>T;
    for(lol i=0; i<T; i++){

       cin>>N>>K;
    occupied.push_back(0);
    occupied.push_back(N+1);


    for(lol j = 0; j < K; j++){

        sort(occupied.begin(),occupied.end());
        lol gr = greatest_diff();
       // cout<<"gr = "<<gr<<endl;
        occupied.push_back((occupied[gr] + occupied[gr+1])/2);

        if(j == K-1){
            lol ans;
            lol pivot = occupied[occupied.size()-1];
            sort(occupied.begin(),occupied.end());
            for(lol iter = 0; iter < occupied.size(); iter++)
                  if(occupied[iter] == pivot){
                      ans = iter;
                      break;}

            cout<<"Case #"<<i+1<<": "<<occupied[ans+1]-occupied[ans]-1<<" "<<(occupied[ans]-occupied[ans-1]-1)<<endl;
             occupied.clear();

        }

        //cout<<endl<<"grdiff = "<<(occupied[gr] + occupied[gr+1])/2<<endl;
        // for(lol k : occupied)
         //cout<<k<<"\t";
    }




    }




    return 0;
}
