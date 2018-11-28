#include <fstream>
#include <vector>
#include <map>
#include <functional>
#include <iostream>

typedef unsigned long long ull;
typedef long long ll;

using namespace std;

int main()
{
    ifstream ifs("B-small-attempt0.in");
    ofstream ofs("B-small-attempt0.out");

    int T;
    ifs >> T;


    for(int i=0; i<T; i++)
    {
        int N;
        int numR = 0, numY = 0, numB = 0, numO = 0, numG = 0, numV = 0;
        ifs >> N >> numR >> numO >> numY >> numG >> numB >> numV;

        // small
        bool possible = !((numR > numY+numB) || (numY > numR+numB) || (numB > numR+numY));

        if(possible)
        {
            vector<char> res;
            if(numR>=numY && numR>=numB)
            {
                res.push_back('R');
                numR--;
            }
            else if(numY>=numR && numY>=numB)
            {
                res.push_back('Y');
                numY--;
            }
            else
            {
                res.push_back('B');
                numB--;
            }

            while(numR>0 || numY>0 || numB>0)
            {
                if(numR<=1 && numY<=1 && numB<=1)
                {
                    if(res[res.size()-1]=='R')
                    {
                        if(numY==1 && numB==1)
                        {
                            if(res[0]=='Y')
                            {
                                res.push_back('Y');
                                res.push_back('B');
                                if(numR>0) res.push_back('R');
                            }
                            else
                            {
                                res.push_back('B');
                                if(numR>0) res.push_back('R');
                                res.push_back('Y');
                            }
                        }
                        else if(numY==1)
                        {
                            res.push_back('Y');
                            if(numR>0) res.push_back('R');
                        }
                        else if(numB==1)
                        {
                            res.push_back('B');
                            if(numR>0) res.push_back('R');
                        }
                    }
                    else if(res[res.size()-1]=='Y')
                    {
                        if(numR==1 && numB==1)
                        {
                            if(res[0]=='R')
                            {
                                res.push_back('R');
                                res.push_back('B');
                                if(numY>0) res.push_back('Y');
                            }
                            else
                            {
                                res.push_back('B');
                                if(numY>0) res.push_back('Y');
                                res.push_back('R');
                            }
                        }
                        else if(numR==1)
                        {
                            res.push_back('R');
                            if(numY>0) res.push_back('Y');
                        }
                        else if(numB==1)
                        {
                            res.push_back('B');
                            if(numY>0) res.push_back('Y');
                        }
                    }
                    else
                    {
                        if(numR==1 && numY==1)
                        {
                            if(res[0]=='R')
                            {
                                res.push_back('R');
                                res.push_back('Y');
                                if(numB>0) res.push_back('B');
                            }
                            else
                            {
                                res.push_back('Y');
                                if(numB>0) res.push_back('B');
                                res.push_back('R');
                            }
                        }
                        else if(numR==1)
                        {
                            res.push_back('R');
                            if(numB>0) res.push_back('B');
                        }
                        else if(numY==1)
                        {
                            res.push_back('Y');
                            if(numB>0) res.push_back('B');
                        }
                    }

                    numR = numY = numB = 0;
                }
                else if(numR>0 && numR>=numY && numR>=numB && res[res.size()-1]!='R')
                {
                    res.push_back('R');
                    numR--;
                }
                else if(numY>0 && numY>=numR && numY>=numB && res[res.size()-1]!='Y')
                {
                    res.push_back('Y');
                    numY--;
                }
                else if(numB>0 && numB>=numR && numB>=numY && res[res.size()-1]!='B')
                {
                    res.push_back('B');
                    numB--;
                }
                else if(numR>0 && (numR>=numY || numR>=numB) && res[res.size()-1]!='R')
                {
                    res.push_back('R');
                    numR--;
                }
                else if(numY>0 && (numY>=numR || numY>=numB) && res[res.size()-1]!='Y')
                {
                    res.push_back('Y');
                    numY--;
                }
                else if(numB>0 && (numB>=numR || numB>=numY) && res[res.size()-1]!='B')
                {
                    res.push_back('B');
                    numB--;
                }
                else if(numR>0 && res[res.size()-1]!='R')
                {
                    res.push_back('R');
                    numR--;
                }
                else if(numY>0 && res[res.size()-1]!='Y')
                {
                    res.push_back('Y');
                    numY--;
                }
                else if(numB>0 && res[res.size()-1]!='B')
                {
                    res.push_back('B');
                    numB--;
                }

                //cout << "R=" << numR << ", Y=" << numY << ", B=" << numB << endl;
            }

            ofs << "Case #" << i+1 << ": ";
            for(int j=0; j<N; j++)
            {
                ofs << res[j];
            }
            ofs << endl;
        }
        else
        {
            ofs << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
}
