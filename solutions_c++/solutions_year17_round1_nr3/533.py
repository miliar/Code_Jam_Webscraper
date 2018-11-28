#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int test = 1;test<=t;test++)
    {
        long long Hd,Ad,Hk,Ak,B,D;
        cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

        //cout << Hd << " " << Ad << " " << Hk << " " << B << " " << D << endl;
        int answer = 10000;
        if(Ad >= Hk)
        {
            answer = 1;
        }

        for(int debuff = 0; (debuff-1)*D < Ak;debuff++)
        {
            for(int buff = 0;Ad + (buff-1)*B < Hk ;buff++)
            {
                //cout << debuff << " " << buff << endl;
                int turns = 0;
                int heroH = Hd;
                int heroA = Ad;
                int vilH = Hk;
                int vilA = Ak;

                int rem_debuff = debuff;
                int rem_buff = buff;

                while(vilH > 0 and turns < answer)
                {
                    //debuff first
                    if(rem_debuff > 0)
                    {
                        if(vilA - D >= heroH)
                        {
                            //cure
                            heroH = Hd;
                            heroH -= vilA;
                        }
                        else
                        {
                            vilA = vilA - D;
                            heroH -= vilA;
                            rem_debuff--;
                        }
                    }
                    else if(rem_buff > 0)
                    {
                        //cure
                        if(vilA >= heroH)
                        {
                            heroH = Hd;
                            heroH -= vilA;
                        }
                        else
                        {
                            heroA += B;
                            heroH -= vilA;
                            rem_buff--;
                        }
                    }
                    else //Attack
                    {
                        if(vilH > heroA and vilA >= heroH)
                        {
                            heroH = Hd;
                            heroH -= vilA;
                        }
                        else
                        {
                            vilH -= heroA;
                            heroH -= vilA;
                        }
                    }
                    turns++;
                }

                answer = min(answer,turns);
                if(B==0)
                {
                    break;
                }
            }

            if(D==0)
            {
                break;
            }
        }
        if(answer == 10000)
        {
            cout << "Case #" << test << ": " <<  "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << test << ": " <<  answer << endl;
        }

    }
}
