#include<iostream>
#include <iomanip>
//std::setw(6);

using namespace std;

int main()
{
  int t;
  cin>>t; // number of testcases
  for(int i=0;i<t;i++)
  {
    double a,b; // ith horse position and speed
    double d,n; // total_distance, number of horses
    cin>>d>>n;


    double maxspeed=-1,speed;

    while(n-->0)
    {
      cin>>a>>b;
      //cout<<(double)(d-a)<<"   ";
      speed = (double)(d-a)/b;
      if(maxspeed < speed)
        maxspeed = speed;
    }
    double result = (double)d/maxspeed;
    //cout.setw(6);
    cout<<"Case #"<<i+1<<": ";
    printf("%f", result);
    cout<<endl;
  }
  return 0;
}

//100.0 - 100 0.0 == 0
