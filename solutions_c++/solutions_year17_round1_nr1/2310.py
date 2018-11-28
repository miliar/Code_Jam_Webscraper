#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;
ifstream myfile;
ofstream myfile2;

typedef vector <char> columns;
vector <columns> Cake;


void init (int rows, int colns)
{
    Cake.clear();
    Cake=vector<columns>();
    columns columnsAdded;
    for (int i=0; i<rows; i++)
    {
        columnsAdded.clear();
        columnsAdded=columns ();
        for (int t=0; t<colns; t++)
        {
            columnsAdded.push_back('?');
        }
        Cake.push_back(columnsAdded);
    }
}
void GetInput ()
{

    for (int i=0; i<Cake.size(); i++)
    {

        for (int t=0; t<Cake[i].size(); t++)
        {
            myfile>>Cake[i][t];
        }

    }
}
void output ()
{
    for (int i=0; i<Cake.size(); i++)
    {
        for (int t=0; t<Cake[i].size(); t++)
        {
            myfile2<<Cake [i][t];
        }
        myfile2<<endl;
    }
}


int main()
{

    int numberOfCases=0;
    int rows=0;
    int colns=0;
    char CurrentLetter = ' ';

    myfile.open ("A-large.in");
    myfile2.open ("example.out");

    myfile>>numberOfCases;
    for (int i=0; i<numberOfCases; i++)
    {
        myfile>>rows;
        myfile>>colns;
        init (rows, colns);
        GetInput();

        for (int t=0; t<colns; t++)
        {
            CurrentLetter=' ';
            for (int q=0; q<rows; q++)
            {
                if (CurrentLetter!=' ' && Cake[q][t]=='?')
                {
                    Cake[q][t]=CurrentLetter;
                }
                else if (CurrentLetter!=' ' && Cake[q][t]!='?' && Cake[q][t]!=CurrentLetter)
                {
                    CurrentLetter=Cake[q][t];
                    //break;
                }
                if (CurrentLetter==' ' && Cake[q][t]!='?')
                {
                    CurrentLetter= Cake[q][t];
                }



            }
        }
        for (int t=0; t<colns; t++)
        {
            CurrentLetter=' ';
            for (int q=rows-1; q>=0; q--)
            {
                if (CurrentLetter!=' ' && Cake[q][t]=='?')
                {
                    Cake[q][t]=CurrentLetter;

                }
                else if (CurrentLetter!=' ' && Cake[q][t]!=CurrentLetter && Cake[q][t]!='?')
                {
                    CurrentLetter=Cake[q][t];
                    //break;
                }
                if (CurrentLetter==' ' && Cake[q][t]!='?')
                {
                    CurrentLetter= Cake[q][t];
                }



            }
        }
        for (int q=rows-1; q>=0; q--)
        {
            CurrentLetter=' ';

            for (int t=0; t<colns; t++)
            {
                if (CurrentLetter!=' ' && Cake[q][t]=='?')
                {
                    Cake[q][t]=CurrentLetter;

                }
                else if (CurrentLetter!=' ' && Cake[q][t]!=CurrentLetter && Cake[q][t]!='?')
                {
                    CurrentLetter=Cake[q][t];
                    //break;
                }
                if (CurrentLetter==' ' && Cake[q][t]!='?')
                {
                    CurrentLetter= Cake[q][t];
                }



            }
        }
        for (int q=rows-1; q>=0; q--)
        {
            CurrentLetter=' ';

            for (int t=colns-1; t>=0; t--)
            {
                if (CurrentLetter!=' ' && Cake[q][t]=='?')
                {
                    Cake[q][t]=CurrentLetter;

                }
                else if (CurrentLetter!=' ' && Cake[q][t]!=CurrentLetter && Cake[q][t]!='?')
                {
                    CurrentLetter=Cake[q][t];
                    //break;
                }
                if (CurrentLetter==' ' && Cake[q][t]!='?')
                {
                    CurrentLetter= Cake[q][t];
                }



            }
        }


        myfile2<<"Case #"<<i+1<<":"<<endl;
        output();

    }


    return 0;
}


