#include <bits/stdc++.h>

using namespace std;

template<typename T>
ostream& operator<<(ostream& o, const vector<T>& v)
{
    o << "[";
    for(size_t i = 0; i < v.size(); i++)
    {
        o << v[i];
        if(i != v.size() - 1)
            o << ", ";
    }
    o << "]";
    return o;
}

class game
{
public:
    int my_attack;
    int my_hp;
    int foe_attack;
    int foe_hp;
    int turn;
    bool operator<(const game& o) const
    {
        if(my_attack != o.my_attack)
            return my_attack < o.my_attack;
        if(my_hp != o.my_hp)
            return my_hp < o.my_hp;
        if(foe_attack != o.foe_attack)
            return foe_attack < o.foe_attack;
        if(foe_hp != o.foe_hp)
            return foe_hp < o.foe_hp;
        return false;
    }
};

int main()
{
    size_t num_cases;
    cin >> num_cases;
    vector<array<int, 6>> input(num_cases);
    vector<int> output(num_cases);
    for(size_t caso = 0; caso < num_cases; caso++)
    {
        for(size_t i = 0; i < 6; i++)
        {
            cin >> input[caso][i];
        }
    }
    #pragma omp parallel for schedule(dynamic)
    for(size_t caso = 0; caso < num_cases; caso++)
    {
        set<game> done;
        game initial;
        initial.my_hp = input[caso][0];
        initial.my_attack = input[caso][1];
        initial.foe_hp = input[caso][2];
        initial.foe_attack = input[caso][3];
        initial.turn = 0;
        queue<game> q;
        q.push(initial);
        bool won = false;
        size_t turns;
        while(!q.empty())
        {
            auto now = q.front();
            q.pop();
            if(done.count(now))
                continue;
            done.insert(now);
            //cerr << "Turn " << now.turn << ": (" << now.my_hp << " / " << now.my_attack << ") - (" << now.foe_hp << " / " << now.foe_attack << ")" << endl;
            if(now.foe_hp <= 0)
            {
                won = true;
                turns = now.turn;
                break;
            }
            if(now.my_hp <= 0)
                continue;
            // Attack
            game attack = now;
            attack.turn++;
            attack.foe_hp = max(attack.foe_hp - attack.my_attack, 0);
            attack.my_hp = max(attack.my_hp - attack.foe_attack, 0);
            if(!done.count(attack))
                q.push(attack);
            // Buff
            if(now.my_attack < now.foe_hp && input[caso][4] != 0)
            {
                game buff = now;
                buff.turn++;
                buff.my_attack += input[caso][4];
                buff.my_hp = max(buff.my_hp - buff.foe_attack, 0);
                if(!done.count(buff))
                    q.push(buff);
            }
            // Debuff
            if(now.foe_attack > 0 && input[caso][5] != 0)
            {
                game debuff = now;
                debuff.turn++;
                debuff.foe_attack = max(debuff.foe_attack - input[caso][5], 0);
                debuff.my_hp = max(debuff.my_hp - debuff.foe_attack, 0);
                if(!done.count(debuff))
                    q.push(debuff);
            }
            // Restore HP
            if(now.my_hp < input[caso][0])
            {
                game restore = now;
                restore.turn++;
                restore.my_hp = input[caso][0];
                restore.my_hp = max(restore.my_hp - restore.foe_attack, 0);
                if(!done.count(restore))
                    q.push(restore);
            }
        }
        if(won)
        {
            output[caso] = turns;
        }
        else
        {
            output[caso] = -1;
        }
        cerr << "Case #" << caso + 1 << endl;
    }
    for(size_t caso = 0; caso < num_cases; caso++)
    {
        cout << "Case #" << caso + 1 << ": " << ((output[caso] >= 0) ? (to_string(output[caso])) : ("IMPOSSIBLE"s)) << endl;
    }
    return 0;
}
