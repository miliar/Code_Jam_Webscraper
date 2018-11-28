#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream inFile;
    ofstream outFile;

 //   inFile.open("in.dat");
    inFile.open("A-large.in");
    outFile.open("out.dat");

    int T;
    inFile>>T;

    for (int main=0;main<T;main++)
    {
  //      cout<<"case "<<main+1<<endl;
        int row, col;
        inFile>>row;
        inFile>>col;

        char cake[row][col];

        //read in array
        for (int k=0;k<row;k++)
            for (int j=0;j<col;j++)
                inFile>>cake[k][j];

    /*    for (int k=0;k<row;k++)
            {
                for (int j=0;j<col;j++)
                    cout<<cake[k][j];
                cout<<endl;
            }*/

        vector<char> usedLetter;

        for (int k=0;k<row;k++)
            for (int j=0;j<col;j++)
            {
                char cur = cake[k][j];
                bool letterAlreadyUsed=false;

                for (int p=0;p<usedLetter.size();p++)
                    if (cur==usedLetter.at(p))
                        letterAlreadyUsed=true;


                if (cur!='?'&&!letterAlreadyUsed)
                {
                    //copy up row
                    int r=j;
                    int s=j;
                    int f=j;
                    while (r-1>=0 && cake[k][r-1]=='?')
                    {
                        cake[k][r-1]=cur;
                        r--;
                        s--;
                   /*     for (int k=0;k<row;k++)
                        {
                            for (int j=0;j<col;j++)
                                cout<<cake[k][j];
                            cout<<endl;
                        }*/
                    }
                    r=j;
                    //copy down row
                    while (r+1<col && cake[k][r+1]=='?')
                    {
                        cake[k][r+1]=cur;
                        r++;
                        f++;
                      /*  for (int k=0;k<row;k++)
                        {
                            for (int j=0;j<col;j++)
                                cout<<cake[k][j];
                            cout<<endl;
                        }*/
                    }

                    //copy entire row
                    bool canCopyDown=true;
                    int d=k;
                    while (canCopyDown)
                    {
                        for (int c=s;c<=f;c++)
                            if (cake[d+1][c]!='?')
                                canCopyDown=false;

                        if (canCopyDown)
                        {
                       //     cout<<"Copying down"<<endl;
                            for (int c=s;c<=f;c++)
                                cake[d+1][c]=cur;
                            d++;
                       /*     for (int k=0;k<row;k++)
                            {
                                for (int j=0;j<col;j++)
                                    cout<<cake[k][j];
                                cout<<endl;
                            }*/
                        }
                    }

                    bool canCopyUp=true;
                    d=k;
                    while (canCopyUp)
                    {
                        for (int c=s;c<=f;c++)
                            if (cake[d-1][c]!='?')
                                canCopyUp=false;

                        if (canCopyUp)
                        {
                        //    cout<<"Copying up"<<endl;
                            for (int c=s;c<=f;c++)
                                cake[d-1][c]=cur;
                            d--;
                     /*       for (int k=0;k<row;k++)
                            {
                                for (int j=0;j<col;j++)
                                    cout<<cake[k][j];
                                cout<<endl;
                            }*/
                        }
                    }
                usedLetter.push_back(cur);

            }
        }
        outFile<<"Case #"<<main+1<<":"<<endl;
        //print array here
        for (int k=0;k<row;k++)
        {
            for (int j=0;j<col;j++)
                outFile<<cake[k][j];
            outFile<<endl;
        }
        //print array
        /*
        cout<<"End of case"<<endl;
        for (int k=0;k<row;k++)
        {
            for (int j=0;j<col;j++)
                cout<<cake[k][j];
            cout<<endl;
        }
        cout<<endl;*/
    }



    inFile.close();
    outFile.close();

    return 0;
}
