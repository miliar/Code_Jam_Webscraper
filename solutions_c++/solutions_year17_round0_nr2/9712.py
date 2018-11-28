#include <bits/stdc++.h>
#include <windows.h>
using namespace std;

int main()
{
    long long cases, num, check = 0, temp, tempCheck = 1, tempNum = 0, cnt = 0;
    stringstream ss;
    istringstream buffer;
    string numStr, tempStr = "";
    vector<long long> result;
    cin >> cases;

    for(int i = 0; i < cases; ++i)
    {
        cin >> num;

        tempNum = 0;
        tempStr = "";
        buffer.clear();
        tempCheck = 1;

        while(check == 0)
        {
            ++cnt;
            ss << num;
            numStr = ss.str();
            ss.str("");

            for(int j = 0; j < numStr.size(); ++j)
            {
                if(j != numStr.size() - 1)
                {
                    if(numStr[j] > numStr[j+1])
                    {
                        temp = j;
                        tempCheck = 0;
                        break;
                    }
                }
            }

            if(tempCheck == 1) break;

            //cout << "temp = " << temp << endl;




            /*for(int j = numStr.size() - 1; j >= temp + 1; --j)
            {
                tempNum += (numStr[j]-48)*round(pow(10,numStr.size()-1-j));
            }*/


            for(int j = temp+1; j < numStr.size(); ++j)
            {
                tempStr += numStr[j];
            }

            buffer.str(tempStr);
            buffer >> tempNum;


            //cout << "tempNum + 1 = " << tempNum + 1 << endl;
            //cout << "num bef = " << num << endl;
            num -= (tempNum + 1);
            //cout << "num aft = " << num << endl;
            tempNum = 0;
            tempStr = "";
            buffer.clear();
            tempCheck = 1;
            //cout << "---------------" << endl;
            //if(cnt == 18) break;
        }
        //cout << "num res = " << num << endl;
        result.push_back(num);
    }
    for(int i = 0; i < result.size(); ++i)
    {
        cout << "Case #" << i+1 << ": " << result[i] << endl;
    }
}
