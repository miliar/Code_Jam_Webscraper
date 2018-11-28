#include<iostream>
#include<string>
#include<fstream>

using namespace std;

long long int cake(string s,int k) { long long int flips=0;
                                                int flag=0;

                                         for(int i=0;i<s.size();i++)
                                         {
                                           if(s[i]=='+')
                                              continue;
                                           else if(i+k <=s.size())
                                             {    flips++;
                                                  for(int j=0;j<k;j++)
                                                {
                                                    if(s[i+j]=='-')
                                                        s[i+j]='+';
                                                    else
                                                        s[i+j]='-';
                                                }

                                            }
                                            else
                                            {
                                                flag=1;
                                            }

                                         }
                                         for(int i=0;i<s.size();i++)
                                         {  if(s[i]=='-')
                                             {
                                                 flag=1;
                                                 break;
                                             }
                                         }
                                         if(flag==1)
                                            return -1;
                                         else
                                            return flips;

                          }

int main(){   ifstream in("input.in");
               ofstream out("output.in");
               long long int t,a;
               in>>t;
               for(a=1;a<t+1;a++)
               {
                     string s;
                     long long int k,n;
                     in>>s;
                     in>>k;
                   n=cake(s,k);
                   if(n==-1)
                     out<<"Case #"<<a<<": IMPOSSIBLE"<<endl;
                   else
                   out<<"Case #"<<a<<": "<<n<<endl;

               }
        cout<<endl;
         return 0;
          }
