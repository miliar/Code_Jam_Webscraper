#include <QMap>
#include <QTextStream>

typedef long long intL;

QString solve(intL N, intL K)
{
    QMap<intL, intL> D; // size, count
    D[N] = 1;
    --K; // calc last one separetly
    while (K > 0)
    {
        intL lastR = D.lastKey(); // Range size
        if (lastR == 1) // shortcut; if reached 1-place region (0,0) is the only possible answer
        {
            return QString("%1 %2").arg(0).arg(0);
        }
        intL cntR = D[lastR];
        intL decr = std::min(cntR, K);
        K -= decr;
        if (cntR == decr)
        {
            D.erase(D.find(lastR));
        }
        else {
            D.last() -= decr;
        }

        // Add new ranges instead of removed one
        D[(lastR - 1) / 2] += decr;
        D[lastR / 2] += decr;
    }

    intL lastR = D.lastKey();

    return QString("%1 %2").arg(lastR / 2).arg((lastR - 1) / 2);
}

int main(int, char**)
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();

    for (int i = 0; i < T; ++i)
    {
        intL N, K;
        ins >> N >> K;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(N, K) << endl;
    }

    return 0;
}
