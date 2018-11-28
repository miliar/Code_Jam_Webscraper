#include <QCoreApplication>
#include <QFile>
#include <QStringList>
#include <QTextStream>
#include <QDebug>
#include <QtGlobal>
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QPair>

bool is_debug = false;

QString getAnswer(QString Str) {
    if (is_debug) {
        qDebug() << "start getAnswer" << Str;
    }

    QString res;
    QList<int> resI;
    bool decreased = false;
    int curr_a, prev_res = -1;
    for(int i = 0, Ln = Str.length(); i < Ln; ++i) {
        curr_a = QString(Str.at(i)).toInt();
        qDebug() << "check" << curr_a << prev_res << decreased << resI;
        if (decreased) {
            qDebug() << "decreased add 9";
            resI.append(9);
        } else if ((curr_a >= prev_res) || (prev_res == -1)) {
            qDebug() << "normal add" << curr_a;
            resI.append(curr_a);
            prev_res = curr_a;
        } else {
            decreased = true;
            int j = i;
            qDebug() << "start decrease" << i << j;
            resI.append(9);
            while(--j >= 0) {
                qDebug() << i << j << resI;
                if (resI.at(j) > 0) {
                    if (--resI[j] > 0) {
                        break;
                    } else if (j > 0) {
                        resI[j] = 9;
                    }
                } else {
                    resI[j] = 9;
                }
            }
        }
    }

    bool first = true;
    foreach(int a, resI) {
        if (first && a == 0) {
            continue;
        }
        first = false;
        res.append(QString::number(a));
    }

    bool normal = true;
    int prev_a = -1;
    foreach(int a, resI) {
        if (prev_a > a) {
            normal = false;
            break;
        }
        prev_a = a;
    }

    return normal ? res : getAnswer(res);//QString::number(res);
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QStringList params = QCoreApplication::arguments();
    if (params.count() < 3) {
        return 1;
    }

    qDebug() << params;
    qDebug() << params.at(1);
    QFile file_in(params.at(1));
    if (!file_in.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return 2;
    }

    QTextStream in(&file_in);

    QFile file_out(params.at(2));
    if (!file_out.open(QIODevice::WriteOnly)) {
        return 3;
    }

    is_debug = true;//params.count() > 3 && params.at(3).compare("debug") == 0;

    QTextStream out(&file_out);
    QString line;
    int Idx = -1;
    int CaseNum = 0;
    QString answer;

    QDateTime start;
    QDateTime finish;
    QStringList sl;
    int line_type = 0;
    int K = 0;
    QString str;

    while (!in.atEnd()) {
        line = in.readLine();
        if (++Idx == 0) {
            if (is_debug) qDebug() << "Input case count " << line;
            continue;
        }


            answer = "Case #" + QString::number(++CaseNum) + ": " + getAnswer(line);
            out << answer;
            endl(out);

        if (is_debug) {
            //qDebug() << "LineProcessed" << finish.toTime_t() - start.toTime_t();
        }

    }//*/
    return 0;
    //return a.exec();
}
