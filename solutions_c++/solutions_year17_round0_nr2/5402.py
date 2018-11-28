#include <string>
#include <iostream>
using namespace std;

//bool verify(int n)
//{
//    char buff[100]={0};
//    sprintf(buff, "%d", n);
//    string p = buff;
//    for(int i=1; i<p.length(); ++i)
//    {
//        if(p[i-1]>p[i]) return false;
//    }
//    return true;
//}
//int main(int argc, char* argv)
//{
//    int T;
//    cin >> T;
//    for(int t=0; t<T; ++t)
//    {
//        int N;
//        cin >> N;
//        int result = N;
//        for(int i=N; i>=0; --i)
//        {
//            if(verify(i))
//            {
//                result = i;
//                break;
//            }
//        }
//        cout << "Case #" << (t+1) << ": ";
//        cout << result << endl;
//    }
//    return 0;
//}

int main(int argc, char* argv)
{
    int T;
    cin >> T;
    for(int t=0; t<T; ++t)
    {
        string N;
        cin >> N;
        string result = N;
        if(N.length()>1) 
        {            
            while(true)
            {
                string prevResult = result;
                for(int i=1; i< prevResult.length(); ++i)
                {
                    if(prevResult[i-1]>prevResult[i])
                    {
                        result[i-1]=result[i-1]-1;
                        for(int j=i; j<result.length(); ++j)
                        {
                            result[j]='9';
                        }
                        break;
                    }
                }
                if(prevResult == result) break;
            }

            string rmvHeadZero;
            for(int i=0; i<result.length(); ++i)
            {
                if(result[i]=='0') continue;
                rmvHeadZero = result.substr(i, result.size()-i);
                break;
            }
            result = rmvHeadZero;
        }
        cout << "Case #" << (t+1) << ": ";
        cout << result << endl;
        
    }
    return 0;
}