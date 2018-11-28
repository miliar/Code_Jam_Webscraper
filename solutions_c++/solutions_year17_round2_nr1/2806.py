#include <QVector>
#include <QList>
#include <QMap>
#include <QtAlgorithms>
#include <QTextStream>
#include <set>
#include <QDebug>

//typedef long long intL;
//typedef long double floatL;

double getMaxS(double D, double P, double S)
{
    double dD = D - P;
    double tF = dD / S;
    return D / tF;
}

double solve(int D, int N, QVector<int>& P, QVector<int>& S)
{
    double ret = -1;

    for (int j = 0; j < N; ++j)
    {
        double cur = getMaxS(D, P[j], S[j]);
        if (ret < 0)
        {
            ret = cur;
        }
        else
        {
            ret = std::min(ret, cur);
        }
    }

    return ret;
}

int main(int, char**)
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();

    for (int i = 0; i < T; ++i)
    {
        int N, D;
        ins >> D >> N;
        QVector<int> P(N), S(N);
        for (int j = 0; j < N; ++j)
        {
            ins >> P[j] >> S[j];
        }
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(D, N, P, S), -8,'f', 6) << endl;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(N, P, R, Q) << endl;
    }

    return 0;
}
