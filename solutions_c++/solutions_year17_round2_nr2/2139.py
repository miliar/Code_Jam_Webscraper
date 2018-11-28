#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;
ifstream myfile;
ofstream myfile2;

enum {R=0,O,Y,G,B,V};


bool done (int manes[V+1])
{
    //t counter=0;

    for (int i=0; i<V+1; i++)
    {
        if (manes[i]!=0)
        {
            return false;
        }
    }

    return true;
}


int main()
{

    int numberOfCases=0;
    int NumberOfUni=0;
    int manes [V+1];
    bool impossible=false;
    string order="";
    map <int,int> ColourMap;
    map <int,char> ColourMapToChar;
    map <char,int> ColourMapToInt;

    ColourMap [G]=R;
    ColourMap [O]=B;
    ColourMap [V]=Y;

    ColourMapToChar[R]='R';
    ColourMapToChar[O]='O';
    ColourMapToChar[Y]='Y';
    ColourMapToChar[G]='G';
    ColourMapToChar[B]='B';
    ColourMapToChar[V]='V';
    ColourMapToInt['R']=R;
    ColourMapToInt['O']=O;
   ColourMapToInt['Y']=Y;
    ColourMapToInt['G']=G;
    ColourMapToInt['B']=B;
    ColourMapToInt['V']=V;



    myfile.open ("B-small-attempt0.in");
    myfile2.open ("example.out");

    myfile>>numberOfCases;
    for (int i=0; i<numberOfCases; i++)
    {
        impossible=false;
        order="";
        myfile>>NumberOfUni;
        for (int t=0; t<=V; t++)
        {
            myfile>>manes[t];

        }
        while (!done(manes))
        {
            if (manes[O]!=0 && ColourMapToInt[order[order.length()-1]]==ColourMap [O] )
            {
                order+=ColourMapToChar[O];
                manes[O]--;
                if (manes[ColourMap [O]]!=0)
                {
                    order+=ColourMapToChar[ColourMap [O]];
                    manes[ColourMap [O]]--;
                }
                else if (!done(manes))
                {
                    myfile2<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
                    break;
                }

            }
            else if (manes[G]!=0 && ColourMapToInt[order[order.length()-1]]==ColourMap [G] )
            {
                order+=ColourMapToChar[G];
                manes[G]--;
                if (manes[ColourMap [G]]!=0)
                {
                    order+=ColourMapToChar[ColourMap [G]];
                    manes[ColourMap [G]]--;
                }
                else if (!done(manes))
                {
                    myfile2<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
                    impossible=true;
                    break;
                }
            }
            else if (manes[V]!=0 && ColourMapToInt[order[order.length()-1]]==ColourMap [V] )
            {
                order+=ColourMapToChar[V];
                manes[V]--;
                if (manes[ColourMap [V]]!=0)
                {
                    order+=ColourMapToChar[ColourMap [V]];
                    manes[ColourMap [V]]--;
                }
                else if (!done(manes))
                {
                    myfile2<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
                    impossible=true;
                    break;
                }
            }
            else
            {
                if (manes[B]!=0 && ColourMapToInt[order[order.length()-1]]!=B )
                {
                    order+=ColourMapToChar[B];
                    manes[B]--;
                }
                else if (manes[Y]!=0 && ColourMapToInt[order[order.length()-1]]!=Y && manes[Y]>=manes[R])
                {
                    order+=ColourMapToChar[Y];
                    manes[Y]--;
                }
                else if (manes[R]!=0 && ColourMapToInt[order[order.length()-1]]!=R)
                {
                    order+=ColourMapToChar[R];
                    manes[R]--;
                }
                else
                {
                    myfile2<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
                    impossible=true;
                    break;

                }
            }

        }
        if (impossible==false)
        {
            if (order[0]!=order[order.length()-1])
            {
                myfile2<<"Case #"<<i+1<<": "<<order<<endl;
            }
            else
            {
                myfile2<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
            }

        }
        else
        {
            //cout<<"Case #"<<i+1<<": "<<order<<endl;
        }


    }
return 0;
}

