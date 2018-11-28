#include<iostream>
#include<iomanip>
#include<fstream>

using namespace std;



int main(){   ifstream in("input.in");
               ofstream out("output.in");
               long long int t,a;
               in>>t;
               for(a=1;a<t+1;a++)
               {

                     long long int noh;
                      double dt,frstp,frstv,maxt,vel;

                      in>>dt;
                      in>>noh;
                      in>>frstp;
                      in>>frstv;
                      maxt = (dt - frstp) / frstv;
                     for(int i=1;i<noh;i++)
                         {  double p,v,t;
                            in>>p;
                             in>>v;
                            t = (dt-p)/v;
                            if(t>maxt)
                            {
                                maxt=t;
                            }
                          }

                        vel = dt/maxt;


                    out<<fixed;

                   out<<"Case #"<<a<<": "<<setprecision(6)<<vel<<endl;

               }
        out<<endl;
         return 0;
          }
