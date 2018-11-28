#include<iostream>
#include<string>
#include<fstream>
#include<math.h>

using namespace std;

unsigned long long power(int b, int p) {  if(p==0 || b==1)
                                              return 1;
                                           else
                                           {   unsigned long long int bb=b;
                                               for(int i=1;i<p;i++)
                                                   bb=bb*b;
                                               return bb;
                                           }


                                           }
int perfect( unsigned long long int no){      int nd = log10(no)+1;
                                   unsigned long long int t=no,pp;
                                       pp=(power(10,nd-1));
                                       int m= no/pp;
                                    for(int i=1;i<nd+1;i++)
                                        {   int d = t/pp;
                                            t=t%pp;
                                            pp = pp/10;
                                            if(d==0)
                                                return 0;
                                            if(d>=m)
                                            { m=d;
                                              continue;
                                             }
                                             else
                                             {   return 0;
                                                 break;
                                             }
                                        }

                                          return 1; }


unsigned long long int tidy (unsigned long long int no){ unsigned long long int n = no;
                                                      int nd = log10(no)+1;
                                                         int arr[nd+1];
                                                      /* REMOVE ALL ZEROES */
                                                          unsigned long long int t=no,pp;
                                                              pp=(power(10,nd-1));

                                                      for(int i=1;i<nd+1;i++)
                                                          {         arr[i]= t/pp;
                                                                   t=t%pp;
                                                                    pp = pp/10;
                                                          }

                                                      for(int i=2;i<nd+1;i++)
                                                      {  if(arr[i]==0)
                                                        {      for(int j=i;j<nd+1;j++)
                                                                     arr[j]=9;
                                                               for(int k=i-1;k>0;k--)
                                                               {  if(arr[k]==1 && k!=1)
                                                                      {arr[k]=9;
                                                                       continue;
                                                                      }
                                                                   else if(arr[k]==1 && k==1)
                                                                        arr[k]=0;
                                                                   else {
                                                                       arr[k]=arr[k]-1;
                                                                       break;
                                                                       }

                                                                 }
                                                           break;
                                                           }
                                                      }
                                                      n=0;
                                                    for(int i=1;i<nd+1;i++ )
                                                    {
                                                        n=n+(arr[i]*power(10,nd-i));
                                                    }

                                                    /* Let's Play with other guys */
                                                   if( perfect(n))
                                                       return n;
                                                   else
                                                   {   nd = log10(n)+1;
                                                         int arr2[nd+1];
                                                         t=n;
                                                         pp=(power(10,nd-1));
                                                       for(int i=1;i<nd+1;i++)
                                                          {         arr2[i]= t/pp;
                                                                   t=t%pp;
                                                                    pp = pp/10;
                                                          }
                                                          for(int i=nd;i>1;i--)
                                                          {
                                                              if(arr2[i]<arr2[i-1])
                                                              { for(int j=i;j<nd+1;j++)
                                                                    arr2[j]=9;
                                                                  arr2[i-1]=arr2[i-1]-1;
                                                              }
                                                          }

                                                  n=0;
                                                  for(int i=1;i<nd+1;i++ )
                                                    {
                                                        n=n+(arr2[i]*power(10,nd-i));
                                                    }

                                                      return n;


                                                       }


                                                    }
int main(){   ifstream in("input.in");
               ofstream out("output.in");
               long long int t,a;
               in>>t;
               for(a=1;a<t+1;a++)
               {

                    unsigned long long int no,n,p;
                        in>>no;
                        n = tidy(no);
                        out<<"Case #"<<a<<": "<<n<<endl;

                 }
            out<<endl;
         return 0;
          }
